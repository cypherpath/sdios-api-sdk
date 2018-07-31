"""SharingDriver class object"""
from typing import Optional

from api.base_driver import BaseDriver
from api.driver import APIDriver
from api.driver import APIResponse
from settings.urls import APICategory


class SharingDriver(BaseDriver):
    """Make all network API calls."""
    _category = APICategory.SHARING

    def __init__(self, api_driver: APIDriver) -> None:
        """Initialize SharingDriver class

        :param api_driver: Allows SharingDriver to communicate with SDI OS
        :type api_driver: APIDriver class object
        """
        super().__init__(api_driver)
        self.user_pk = None # type: Optional[int]

    def clear(self) -> None:
        """Clear pks."""
        self.user_pk = None # type: Optional[int]

    def get_all_shared(self) -> APIResponse:
        """Get users/groups shared networks and return response."""
        return self._get("network_list")

    def get_all_users_shared(self) -> APIResponse:
        """Get all user's shared networks and return response."""
        return self._get("user_list")

    def get_user_shared(self, user_pk: int = None) -> APIResponse:
        """Get a user's shared networks and return response.

        :param user_pk: Pk of user to look up shared networks. Default is self.user_pk.
        :type user_pk: int
        """
        url_args = {"pk": self.user_pk if user_pk is None else user_pk}
        return self._get("user_detail", url_args)

    def get_all_groups_shared(self) -> APIResponse:
        """Get all group's shared networks and return response."""
        return self._get("group_list")

    def get_group_shared(self, group_pk: int) -> APIResponse:
        """Get group's shared networks and return response."""
        return self._get("group_detail", {"group_pk": group_pk})
