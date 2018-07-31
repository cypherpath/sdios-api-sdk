"""SettingsDriver class object"""
from typing import Any, Dict

from api.base_driver import BaseDriver
from api.driver import APIDriver
from api.driver import APIResponse
from settings.urls import APICategory


class SettingsDriver(BaseDriver):
    """Make all system settings API calls."""
    _category = APICategory.SYSTEM_SETTINGS

    def __init__(self, api_driver: APIDriver) -> None:
        """Initialize SettingsDriver class

        :param api_driver: Allows SettingsDriver to communicate with SDI OS
        :type api_driver: APIDriver class object
        """
        super().__init__(api_driver)

    def get_settings(self) -> APIResponse:
        """Get system settings and return response."""
        return self._get("detail")

    def modify_settings(self, data: Dict[str, Any]) -> APIResponse:
        """Modify system settings and return response."""
        return self._put("detail", data=data)

    def get_physical_networks(self) -> APIResponse:
        """Get physical networks on SDI OS and return response."""
        return self._get("physical_networks")

    def modify_physical_networks(self, data: Dict[str, Any]) -> APIResponse:
        """Modify physical network settings and return response."""
        return self._put("physical_networks", data=data)

    def get_license(self) -> APIResponse:
        """Get license for SDI OS and return response."""
        return self._get("license")

    def get_ssl(self) -> APIResponse:
        """Get ssl certificate for SDI OS and return response."""
        return self._get("ssl")

    def modify_ssl(self, ssl_files) -> APIResponse:
        """Modify ssl certificate on SDI OS and return response."""
        return self._put("ssl", files=ssl_files)

    def get_version(self) -> APIResponse:
        """Get SDI OS version and return response."""
        return self._get("version")
