"""APIDriver class object"""
from typing import Any, Dict, List, Optional, Tuple, Union

import ast
import io
import json
import sys
import time
from enum import Enum

import requests
from semantic_version import Version

import settings.general as g_settings
import settings.urls as urls
from settings.urls import APICategory

# disable ssl verify warnings
requests.packages.urllib3.disable_warnings()


class APIDriverError(RuntimeError):
    """APIDriver base exception class"""

class APITokenError(RuntimeError):
    """APIToken base exception class"""

class NoTokenError(APITokenError):
    """Raise exception when API token is not found"""
    def __init__(self) -> None:
        super().__init__("No API token found! A token must be created before making any API calls!")

class CreateTokenError(APITokenError):
    """Raise exception when an error is encountered creating a token"""

class RevokeTokenError(APITokenError):
    """Raise exception when an error is encountered revoking a token"""

class NoActiveTokenError(APITokenError):
    """Raise exception when token is not active"""

class InvalidURLError(APIDriverError):
    """Raise exception when API URL is invalid"""

class InvalidVersionError(APIDriverError):
    """Raise exception when API version is invalid"""

def get_json_format_writer() -> io.TextIOWrapper:
    """Return an io.TextIOWrapper with custom JSON formatting wrapper"""
    stdout = sys.stdout


    class JSONTextIOWrapper(io.TextIOWrapper):
        """JSON format wrapper"""
        def __init__(self, *args, **kwargs) -> None:
            super().__init__(*args, **kwargs)

        def write(self, s: str) -> int:
            try:
                if g_settings.JSON_FORMATTING:
                    return super().write(json.dumps(ast.literal_eval(s), indent=g_settings.JSON_FORMAT_INDENT))
                else:
                    raise AssertionError
            except (AssertionError, json.decoder.JSONDecodeError, SyntaxError, TypeError, ValueError):
                return super().write(s)
    return JSONTextIOWrapper(buffer=stdout.buffer, encoding=stdout.encoding, errors=stdout.errors, line_buffering=stdout.line_buffering)

sys.stdout = get_json_format_writer() if g_settings.JSON_FORMATTING else sys.stdout


class HTTPMethod(Enum):
    """Enum class for HTTP Methods"""
    OPTIONS = 1
    GET = 2
    HEAD = 3
    POST = 4
    PUT = 5
    DELETE = 6


class APIResponse:
    """Reponse object for API Driver"""
    def __init__(self, response: requests.Response) -> None:
        self.__response = response

    def __str__(self) -> str:
        padding = 11
        return " {:>{pad}}: {}\n".format("Detail", json.dumps(ast.literal_eval(str(self.detail)), indent=g_settings.JSON_FORMAT_INDENT), pad=padding) + \
               " {:>{pad}}: {}\n".format("Method", self.method, pad=padding) + \
               " {:>{pad}}: {}\n".format("Status Code", self.status_code, pad=padding) + \
               " {:>{pad}}: {}\n".format("Reason", self.reason, pad=padding) + \
               " {:>{pad}}: {}\n".format("Ok", self.ok, pad=padding) + \
               " {:>{pad}}: {}\n".format("URL", self.url, pad=padding) + \
               " {:>{pad}}: {}\n".format("Allow", self.allow, pad=padding)

    @property
    def response(self) -> requests.Response:
        """requests Response object"""
        return self.__response

    @property
    def status_code(self) -> int:
        """Integer Code of responded HTTP Status, e.g. 404 or 200"""
        return self.__response.status_code

    @property
    def reason(self) -> str:
        """Textual reason of responded HTTP Status, e.g. “Not Found” or “OK”."""
        return self.__response.reason

    @property
    def url(self) -> str:
        """Final URL location of APIResponse"""
        return self.__response.url

    @property
    def method(self) -> HTTPMethod:
        """HTTP verb sent to the server"""
        return self.__response.request.method

    @property
    def ok(self) -> bool:
        """Returns True if status_code is less than 400, False if not."""
        return self.__response.ok

    @property
    def allow(self) -> List[str]:
        """List of the set of methods supported by the resource."""
        try:
            return self.__response.headers["Allow"].split(', ')
        except KeyError:
            pass
        return []

    @property
    def detail(self) -> Any:
        """Returns the json-encoded content of the response, if any."""
        try:
            return self.__response.json()
        except (ValueError, KeyError):
            pass
        return None


class APIToken:
    """Oauth API Token object class"""
    def __init__(self, domain: str, credentials: Dict[str, str], api_version: Optional[Version]) -> None:
        self.__domain = domain
        self.__api_version = api_version
        self.__client_id = ""
        self.__client_secret = ""
        self.__is_active = False
        self.__create_time = 0.0
        self.__response = self.__request(credentials)

    def __str__(self) -> str:
        padding = 13
        return "\n {:>{pad}}: {}\n".format("Access Token", self.access_token, pad=padding) + \
               " {:>{pad}}: {}\n".format("Refresh Token", self.refresh_token, pad=padding) + \
               " {:>{pad}}: {}\n".format("Token Type", self.token_type, pad=padding) + \
               " {:>{pad}}: {}\n".format("Expires In", self.expires_in, pad=padding) + \
               " {:>{pad}}: {}\n".format("Time Left", self.time_left, pad=padding) + \
               " {:>{pad}}: {}\n".format("Is Expired", self.is_expired, pad=padding) + \
               " {:>{pad}}: {}\n".format("Is Active", self.is_active, pad=padding)

    @property
    def access_token(self) -> str:
        """String representing an authorization issued to the client."""
        return self.__response.json()["access_token"] if self.is_active else ""

    @property
    def token_type(self) -> str:
        """The type of the token issued by server."""
        return self.__response.json()["token_type"] if self.is_active else ""

    @property
    def expires_in(self) -> int:
        """Lifetime in seconds of the access token."""
        return self.__response.json()["expires_in"] if self.is_active else 0

    @property
    def refresh_token(self) -> str:
        """String representing a credential used to obtain a new access token."""
        return self.__response.json()["refresh_token"] if self.is_active else ""

    @property
    def time_left(self) -> float:
        """Amount in seconds that the token will expire."""
        time_left = self.expires_in - (time.monotonic() - self.__create_time)
        return time_left if time_left > 0 else 0

    @property
    def is_expired(self) -> bool:
        """Boolean if the token is expired."""
        return self.time_left <= 0

    @property
    def is_active(self) -> bool:
        """Boolean if the token has been revoked and cannot be refreshed."""
        return self.__is_active

    @property
    def response(self) -> requests.Response:
        """requests Response object"""
        return self.__response

    def __authenticate(self, payload: Dict[str, str]) -> None:
        headers = {"content_type": "application/json"}
        if self.__api_version is not None:
            headers["Accept"] = "application/json; version={}".format(self.__api_version)

        url = "https://{}:{}@{}/api/o/token/".format(self.__client_id, self.__client_secret, self.__domain)
        response = requests.post(url, data=payload, headers=headers, verify=False)
        if response.ok:
            if self.is_active and not self.is_expired:
                self.revoke()
            self.__create_time = time.monotonic()
            self.__is_active = True
            self.__response = response
        else:
            raise CreateTokenError("Failure to create API token: {}".format(response.text))

    def __request(self, creds: Dict[str, str]) -> requests.Response:
        self.request(creds)
        return self.__response

    def request(self, creds: Dict[str, str]) -> None:
        """Request a new access token.

        :param creds: User's API credentials needed to request a token.
        :type creds: Dict with keys: "username", "password", "client_id", and "client_secret
        """
        self.__client_id = creds["client_id"]
        self.__client_secret = creds["client_secret"]
        payload = {
            "grant_type": "password",
            "username": creds["username"],
            "password": creds["password"],
        }
        self.__authenticate(payload)

    def refresh(self) -> None:
        """Use refresh token to request new access token and refresh token"""
        if self.is_active:
            payload = {
                "grant_type": "refresh_token",
                "refresh_token": self.refresh_token,
            }
            self.__authenticate(payload)
        else:
            raise NoActiveTokenError("API token is no longer active. Please request a new token.")

    def revoke(self) -> None:
        """Revoke Oauth token."""
        if self.is_active:
            headers = {"content_type": "application/json",
                       "Authorization": "{} {}".format(self.token_type, self.access_token)}
            if self.__api_version is not None:
                headers["Accept"] = "application/json; version={}".format(self.__api_version)

            payload = {
                # "token_type_hint": "access_token",
                "token": self.access_token,
                "client_id": self.__client_id,
                "client_secret": self.__client_secret
            }
            url = "https://{}/api/o/revoke_token/".format(self.__domain)
            response = requests.post(url, data=payload, headers=headers, verify=False)

            if response.ok:
                self.__is_active = False
                self.__response = response
            else:
                raise RevokeTokenError("Failure to revoke API token: {}".format(response.text))
        else:
            raise NoActiveTokenError("API token is no longer active. Please request a new token.")

class APIDriver:
    """Authenticate with SDI OS and contain methods to make API calls."""

    def __init__(self, domain: str, credentials: Dict[str, str], api_version: Optional[str]) -> None:
        """Initialize APIDriver class object.

        :param domain: IP address or domain name of server.
        :type domain: str or unicode
        :param credentials: User's API credentials needed to request a token.
        :type credentials: Dict with keys: "username", "password", "client_id", and "client_secret
        :param api_version: Version number for API urls.
        :type api_version: str
        """
        self.api_version = api_version
        self.domain = domain
        self.__token = APIToken(self.domain, credentials, self.__api_version)
        self.__api_version = None # type: Optional[Version]

    @property
    def api_version(self) -> Optional[str]:
        """String of the API version APIDriver uses to make calls."""
        return str(self.__api_version) if self.__api_version is not None else None

    @api_version.setter
    def api_version(self, version: Optional[str]) -> None:
        if version is not None:
            try:
                self.__api_version = Version.coerce(version) # type: Optional[Version]
            except (ValueError, TypeError):
                raise InvalidVersionError("API version must be entered as a string. e.g. \"2.1.0\"")
        else:
            self.__api_version = None

    @property
    def token(self) -> APIToken:
        """APIToken object that has all Oauth token information."""
        return self.__token

    def get(self, url_dict: Dict[Tuple[str, str], str], url_args: Dict[str, Any] = None) -> APIResponse:
        """Call GET request. Return dictionary response of outcome."""
        version_url = self.__get_version_url(url_dict)
        url = version_url.format(**url_args) if url_args is not None else version_url
        return self.__call_url(url, HTTPMethod.GET)

    def __get_version_url(self, url_dict: Dict[Tuple[str, str], str]) -> str:
        if self.__api_version is None:
            return url_dict[max(url_dict.keys())]
        else:
            for version_key in url_dict.keys():
                if self.__in_range(version_key):
                    return url_dict[version_key]

        raise InvalidURLError("URL not found for API version {}. Most current URL is {}".format(self.__api_version, url_dict[max(url_dict.keys())]))

    def __in_range(self, tuple_range: Tuple[str, str]) -> bool:
        if self.__api_version is not None:
            return self.__get_api_version(tuple_range[0]) <= self.__api_version <= self.__get_api_version(tuple_range[-1])
        return False

    @staticmethod
    def __get_api_version(version: str) -> Version:
        return Version.coerce(version)

    def post(self, url_dict: Dict[Tuple[str, str], str], url_args: Dict[str, Any] = None, data: Dict[str, Any] = None) -> APIResponse:
        """Call POST request. Return APIResponse object."""
        version_url = self.__get_version_url(url_dict)
        url = version_url.format(**url_args) if url_args is not None else version_url
        return self.__call_url(url, HTTPMethod.POST, data=data)

    def put(self, url_dict: Dict[Tuple[str, str], str], url_args: Dict[str, Any] = None, data: Union[List[Dict[str, Any]], Dict[str, Any]] = None,
            files: Dict[str, Any] = None) -> APIResponse:
        """Call PUT request. Return APIResponse object."""
        version_url = self.__get_version_url(url_dict)
        url = version_url.format(**url_args) if url_args is not None else version_url
        return self.__call_url(url, HTTPMethod.PUT, data=data, files=files)

    def delete(self, url_dict: Dict[Tuple[str, str], str], url_args: Dict[str, Any] = None) -> APIResponse:
        """Call DELETE request. Return APIResponse object."""
        version_url = self.__get_version_url(url_dict)
        url = version_url.format(**url_args) if url_args is not None else version_url
        return self.__call_url(url, HTTPMethod.DELETE)

    def options(self, url_dict: Dict[Tuple[str, str], str], url_args: Dict[str, Any] = None) -> APIResponse:
        """Call OPTIONS request. Return APIResponse object."""
        version_url = self.__get_version_url(url_dict)
        url = version_url.format(**url_args) if url_args is not None else version_url
        return self.__call_url(url, HTTPMethod.OPTIONS)

    def head(self, url_dict: Dict[Tuple[str, str], str], url_args: Dict[str, Any] = None) -> APIResponse:
        """Call HEAD request. Return APIResponse object."""
        version_url = self.__get_version_url(url_dict)
        url = version_url.format(**url_args) if url_args is not None else version_url
        return self.__call_url(url, HTTPMethod.HEAD)

    def create_one_time_login(self, user_pk: int, expires: int = 900) -> APIResponse:
        """Return one time user login information in an APIResponse object.

        :param user_pk: Key of user to create the login url for
        :type user_pk: int
        :param expires: Time in seconds until the login expires
        :type expires: int
        :returns: One time use information
        :rtype: Dict
        """
        payload = {"user": user_pk,
                   "expires": expires}
        return self.post(urls.API_URLS[APICategory.AUTHENTICATION]["token"]["url"], data=payload)

    def __build_url(self, relative_url: str) -> str:
        return "https://{}/api/{}".format(self.domain, relative_url)

    def __header(self) -> Dict[str, str]:
        if self.token.is_active:
            headers = {"Authorization": "{} {}".format(self.token.token_type, self.token.access_token)}
        else:
            raise NoActiveTokenError("API token is no longer active. Please request a new token.")

        if self.api_version is not None:
            headers["Accept"] = "application/json; version={}".format(self.api_version)
        return headers

    def __call_url(self, url: str, method: HTTPMethod = HTTPMethod.OPTIONS, data: Union[List[Dict[str, Any]], Dict[str, Any]] = None,
                   files: Dict[str, Any] = None) -> APIResponse:
        if self.token.is_expired:
            self.token.refresh()

        absolute_url = self.__build_url(url)
        headers = self.__header()

        if not data:
            data = {}
        if not files:
            files = {}
            headers["content-type"] = "application/json"

        if method is HTTPMethod.GET:
            response = requests.get(absolute_url, headers=headers, verify=False)
        elif method is HTTPMethod.POST:
            response = requests.post(
                absolute_url, data=json.dumps(data), headers=headers, verify=False)
        elif method is HTTPMethod.PUT:
            if files:
                response = requests.put(absolute_url, files=files, headers=headers, verify=False)
            else:
                response = requests.put(absolute_url, data=json.dumps(data),
                                        headers=headers, verify=False)
        elif method is HTTPMethod.DELETE:
            response = requests.delete(absolute_url, headers=headers, verify=False)
        elif method is HTTPMethod.OPTIONS:
            response = requests.options(absolute_url, headers=headers, verify=False)
        elif method is HTTPMethod.HEAD:
            response = requests.head(absolute_url, headers=headers, verify=False)

        return APIResponse(response)
