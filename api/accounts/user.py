"""UserDriver class object"""
from typing import Any, Dict, Optional

from api.base_driver import BaseDriver
from api.driver import APIDriver
from api.driver import APIResponse
from settings.urls import APICategory


class UserDriver(BaseDriver):
    """Make all user API calls

    Methonds that gets, modifies, or deletes takes an int parameter
    of the user's pk number.
    Creating and modifying methods take a Dict[str, Any] with the
    data fields.
    All methods return a APIResponse with the response data from
    the API.
    """
    _category = APICategory.USERS

    def __init__(self, api_driver: APIDriver) -> None:
        """Initialize UserDriver class object

        :param api_driver: Allows UserDriver to communicate with SDI OS
        :type api_driver: APIDriver class object
        """
        super().__init__(api_driver)
        self.tenancy_pk = None # type: Optional[int]

    def clear(self) -> None:
        """Clear pks."""
        self.tenancy_pk = None # type: Optional[int]

    def create(self, data: Dict[str, Any]) -> APIResponse:
        """Create a user/superuser and return response."""
        if "tenancy" not in data:
            data["tenancy"] = self.tenancy_pk
        return self._post("list", data=data)

    def modify(self, key: int, data: Dict[str, Any]) -> APIResponse:
        """Modify a user and return response."""
        return self._put("detail", {"pk": key}, data)

    def delete(self, key: int) -> APIResponse:
        """Delete a user and return response."""
        return self._delete("detail", {"pk": key})

    def get_user(self, key: int) -> APIResponse:
        """Get user's settings and return response."""
        return self._get("detail", {"pk": key})

    def get_all_users(self) -> APIResponse:
        """Get all users in SDI OS and return response."""
        return self._get("list")

    def get_user_pk(self, username: str) -> Optional[int]:
        """Search through get all users and find pk of the matching username."""
        response = self.get_all_users()
        if response.ok:
            user_list = response.detail
            for user in user_list:
                if username == user["username"]:
                    return int(user["pk"])
        return None

    def get_shared_networks(self, key: int) -> APIResponse:
        """Get networks shared with user and return response."""
        return self._get("sharing_networks", {"pk": key})

    def get_shared_sdis(self, key: int) -> APIResponse:
        """Get SDIs shared with user and return response."""
        return self._get("sharing_sdis", {"pk": key})

    def get_shared_disks(self, key: int) -> APIResponse:
        """Get disks shared with user and return response."""
        return self._get("sharing_disks", {"pk": key})
