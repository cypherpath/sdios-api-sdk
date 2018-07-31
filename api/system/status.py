"""StatusDriver class object"""
from api.base_driver import BaseDriver
from api.driver import APIDriver
from api.driver import APIResponse
from settings.urls import APICategory


class StatusDriver(BaseDriver):
    """Make all system status API calls."""
    _category = APICategory.SYSTEM_STATUS

    def __init__(self, api_driver: APIDriver) -> None:
        """Initialize StatusDriver class

        :param api_driver: Allows StatusDriver to communicate with SDI OS
        :type api_driver: APIDriver class object
        """
        super().__init__(api_driver)

    def get_status(self) -> APIResponse:
        """Get status of SDI OS and return response."""
        return self._get("detail")

    def get_nodes(self) -> APIResponse:
        """Get node information and return response."""
        return self._get("nodes")
