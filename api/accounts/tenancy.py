"""TenancyDriver class object"""
from typing import Any, Dict

from api.base_driver import BaseDriver
from api.driver import APIDriver
from api.driver import APIResponse
from settings.urls import APICategory


class TenancyDriver(BaseDriver):
    """Make all tenancy API calls

    Methods that gets, modifies, or deletes takes an int parameter
    of the tenancy's pk number.
    Creating and modifying methods take a Dict[str, Any] with the
    data fields.
    All methods return a APIResponse with the response data from
    the API.
    """
    _category = APICategory.TENANCIES

    def __init__(self, api_driver: APIDriver) -> None:
        """Initialize TenancyDriver class object

        :param api_driver: Allows TenancyDriver to communicate with SDI OS
        :type api_driver: APIDriver class object
        """
        super().__init__(api_driver)

    def create(self, data: Dict[str, Any]) -> APIResponse:
        """Create a tenancy and return response."""
        return self._post("list", data=data)

    def modify(self, key: int, data: Dict[str, Any]) -> APIResponse:
        """Modify a tenancy and return response."""
        return self._put("detail", {"ten_pk": key}, data)

    def delete(self, key: int) -> APIResponse:
        """Delete a tenancy and return response."""
        return self._delete("detail", {"ten_pk": key})

    def get_tenancy(self, key: int) -> APIResponse:
        """Get tenancy's settings and return response."""
        return self._get("detail", {"ten_pk": key})

    def get_security(self, key: int) -> APIResponse:
        """Get tenancy's security settings and return response."""
        return self._get("security", {"ten_pk": key})

    def modify_security(self, key: int, data: Dict[str, Any]) -> APIResponse:
        """Modify a tenancy's secuity settings and return response."""
        return self._put("security", {"ten_pk": key}, data)

    def get_all_tenancies(self) -> APIResponse:
        """Get all tenancies in SDI OS and return response."""
        return self._get("list")
