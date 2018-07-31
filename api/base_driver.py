from typing import Any, Dict, Tuple

import settings.urls as urls
from api.driver import APIDriver, APIResponse
from settings.urls import APICategory


class BaseDriver:
    """Parent class for all component drivers"""
    _category = None # type: APICategory

    def __init__(self, api_driver: APIDriver) -> None:
        self.__api_driver = api_driver

    def __url(self, name: str) -> Dict[Tuple[str, str], str]:
        return urls.API_URLS[self._category][name]["url"]

    def _get(self, name: str, url_args: Dict[str, Any] = None) -> APIResponse:
        return self.__api_driver.get(self.__url(name), url_args)

    def _post(self, name: str, url_args: Dict[str, Any] = None, data: Dict[str, Any] = None) -> APIResponse:
        return self.__api_driver.post(self.__url(name), url_args, data)

    def _put(self, name: str, url_args: Dict[str, Any] = None, data: Any = None, files: Dict[str, Any] = None) -> APIResponse:
        return self.__api_driver.put(self.__url(name), url_args, data, files)

    def _delete(self, name: str, url_args: Dict[str, Any] = None) -> APIResponse:
        return self.__api_driver.delete(self.__url(name), url_args)

    def _options(self, name: str, url_args: Dict[str, Any] = None) -> APIResponse:
        return self.__api_driver.options(self.__url(name), url_args)

    def _head(self, name: str, url_args: Dict[str, Any] = None) -> APIResponse:
        return self.__api_driver.head(self.__url(name), url_args)
