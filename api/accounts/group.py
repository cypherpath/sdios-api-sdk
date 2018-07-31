"""GroupDriver class object"""
from typing import Any, Dict, Optional

from api.base_driver import BaseDriver
from api.driver import APIDriver
from api.driver import APIResponse
from settings.urls import APICategory


class GroupDriver(BaseDriver):
    """Make all group API calls

    Methods that gets, modifies, or deletes takes an int parameter
    of the group's pk number.
    Creating and modifying methods take a Dict[str, Any] with the
    data fields.
    All methods returns a APIResponse with the response data from
    the API.
    """
    _category = APICategory.GROUPS

    def __init__(self, api_driver: APIDriver) -> None:
        """Initialize GroupDriver class object

        :param api_driver: Allows GroupDriver to communicate with SDI OS
        :type api_driver: APIDriver class object
        """
        super().__init__(api_driver)
        self.tenancy_pk = None # type: Optional[int]

    def clear(self) -> None:
        """Clear pks."""
        self.tenancy_pk = None # type: Optional[int]

    def create(self, data: Dict[str, Any]) -> APIResponse:
        """Create a group and return response."""
        if "tenancy" not in data:
            data["tenancy"] = self.tenancy_pk
        return self._post("list", data=data)

    def modify(self, key: int, data: Dict[str, Any]) -> APIResponse:
        """Modify a group and return a response."""
        return self._put("detail", {"group_pk": key}, data)

    def modify_members(self, key: int, data: Dict[str, Any]) -> APIResponse:
        """Add a user member to group and return a response."""
        return self._put("membership", {"group_pk": key}, data)

    def get_members(self, key: int) -> APIResponse:
        """Get members of the group and return a response."""
        return self._get("membership", {"group_pk": key})

    def delete(self, key: int) -> APIResponse:
        """Delete a user and return response."""
        return self._delete("detail", {"group_pk": key})

    def get_group(self, key: int) -> APIResponse:
        """Get groups settings and return response."""
        return self._get("detail", {"group_pk": key})

    def get_all_groups(self) -> APIResponse:
        """Get all groups settings and return response."""
        return self._get("list")
