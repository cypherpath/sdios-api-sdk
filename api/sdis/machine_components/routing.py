"""RoutingDriver class object"""
from typing import Any, Dict, List

from api.sdis.machine_components.base_machine import BaseMachine
from api.driver import APIDriver
from api.driver import APIResponse
from settings.urls import APICategory


class RoutingDriver(BaseMachine):
    """Make all machine routing API calls."""
    _category = APICategory.MACHINE_ROUTING

    def __init__(self, api_driver: APIDriver) -> None:
        """Initialize RoutingDriver class

        :param api_driver: Allows the driver to communicate with SDI OS
        :type api_driver: APIDriver class object
        """
        super().__init__(api_driver)

    def get_routing(self, machine_id: str) -> APIResponse:
        """Get details of managed router and return response."""
        return self._get("detail", {"pk": self.user_pk, "sdi_id": self.sdi_pk, "machine_id": machine_id})

    def get_routing_settings(self, machine_id: str) -> APIResponse:
        """Get managed router settings and return response."""
        return self._get("settings", {"pk": self.user_pk, "sdi_id": self.sdi_pk, "machine_id": machine_id})

    def modify_router_settings(self, machine_id: str, data: Dict[str, Any]) -> APIResponse:
        """Modify managed router settings and return response."""
        return self._put("settings", {"pk": self.user_pk, "sdi_id": self.sdi_pk, "machine_id": machine_id}, data)

    def get_router_keychain(self, machine_id: str) -> APIResponse:
        """Get managed router keychains list and return response."""
        return self._get("keychains", {"pk": self.user_pk, "sdi_id": self.sdi_pk, "machine_id": machine_id})

    def modify_router_keychain(self, machine_id: str, data: List[Dict[str, Any]]) -> APIResponse:
        """Modify managed router keychains and return response."""
        return self._put("keychains", {"pk": self.user_pk, "sdi_id": self.sdi_pk, "machine_id": machine_id}, data)

    def get_router_interfaces(self, machine_id: str) -> APIResponse:
        """Get managed router interfaces and return response."""
        return self._get("interface_list", {"pk": self.user_pk, "sdi_id": self.sdi_pk, "machine_id": machine_id})

    def get_router_interface(self, machine_id: str, conn_id: str) -> APIResponse:
        """Get managed router interface detail and return response."""
        return self._get("interface_detail", {"pk": self.user_pk, "sdi_id": self.sdi_pk, "machine_id": machine_id, "connection_id": conn_id})

    def modify_router_interface(self, machine_id: str, conn_id: str, data: Dict[str, Any]) -> APIResponse:
        """Modify managed router interface and return response."""
        return self._put("interface_detail", {"pk": self.user_pk, "sdi_id": self.sdi_pk, "machine_id": machine_id, "connection_id": conn_id}, data)
