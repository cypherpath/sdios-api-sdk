"""InterfaceDriver class object"""
from typing import Any, Dict

from api.sdis.machine_components.base_machine import BaseMachine
from api.driver import APIDriver
from api.driver import APIResponse
from settings.urls import APICategory


class InterfaceDriver(BaseMachine):
    """Make all machine interface API calls."""
    _category = APICategory.MACHINE_INTERFACES

    def __init__(self, api_driver: APIDriver) -> None:
        """Initialize InterfaceDriver class

        :param api_driver: Allows the driver to communicate with SDI OS
        :type api_driver: APIDriver class object
        """
        super().__init__(api_driver)

    def get_interfaces(self, machine_id: str) -> APIResponse:
        """Get machine's interfaces and return response."""
        return self._get("list", {"pk": self.user_pk, "sdi_id": self.sdi_pk, "machine_id": machine_id})

    def create_interface(self, machine_id: str, data: Dict[str, Any]) -> APIResponse:
        """Create interface for machine and return response."""
        return self._post("list", {"pk": self.user_pk, "sdi_id": self.sdi_pk, "machine_id": machine_id}, data)

    def get_interface(self, machine_id: str, conn_id: str) -> APIResponse:
        """Get interface's detail and return response."""
        return self._get("detail", {"pk": self.user_pk, "sdi_id": self.sdi_pk, "machine_id": machine_id, "connection_id": conn_id})

    def modify_interface(self, machine_id: str, conn_id: str, data: Dict[str, Any]) -> APIResponse:
        """Modify an interface and return a response."""
        return self._put("detail", {"pk": self.user_pk, "sdi_id": self.sdi_pk, "machine_id": machine_id, "connection_id": conn_id}, data)

    def delete_interface(self, machine_id: str, conn_id: str) -> APIResponse:
        """Delete an interface and return a response."""
        return self._delete("detail", {"pk": self.user_pk, "sdi_id": self.sdi_pk, "machine_id": machine_id, "connection_id": conn_id})

    def get_ports(self, machine_id: str, conn_id: str) -> APIResponse:
        """Get the machine's port list and return a response."""
        return self._get("port_list", {"pk": self.user_pk, "sdi_id": self.sdi_pk, "machine_id": machine_id, "connection_id": conn_id})

    def get_vlans(self, machine_id: str, conn_id: str) -> APIResponse:
        """Get the machine's vlan list and return a response."""
        return self._get("vlan_list", {"pk": self.user_pk, "sdi_id": self.sdi_pk, "machine_id": machine_id, "connection_id": conn_id})

    def create_vlan(self, machine_id: str, conn_id: str, data: Dict[str, Any]) -> APIResponse:
        """Create a machine vlan and return response."""
        return self._post("vlan_list", {"pk": self.user_pk, "sdi_id": self.sdi_pk, "machine_id": machine_id, "connection_id": conn_id}, data)

    def get_vlan(self, machine_id: str, conn_id: str, vlan_id: int) -> APIResponse:
        """Get machine's vlan details and return response."""
        return self._get("vlan_detail", {"pk": self.user_pk, "sdi_id": self.sdi_pk, "machine_id": machine_id, "connection_id": conn_id, "vlan_id": vlan_id})

    def modify_vlan(self, machine_id: str, conn_id: str, vlan_id: int, data: Dict[str, Any]) -> APIResponse:
        """Modify machine's vlan and return response."""
        return self._put("vlan_detail", {"pk": self.user_pk, "sdi_id": self.sdi_pk, "machine_id": machine_id, "connection_id": conn_id, "vlan_id": vlan_id}, data)

    def delete_vlan(self, machine_id: str, conn_id: str, vlan_id: int) -> APIResponse:
        """Delete machine's vlan and return response."""
        return self._delete("vlan_detail", {"pk": self.user_pk, "sdi_id": self.sdi_pk, "machine_id": machine_id, "connection_id": conn_id, "vlan_id": vlan_id})

    def get_vlan_ports(self, machine_id: str, conn_id: str, vlan_id: int) -> APIResponse:
        """Get machine's vlan port forwarders and return response."""
        return self._get("vlan_port_list", {"pk": self.user_pk, "sdi_id": self.sdi_pk, "machine_id": machine_id, "connection_id": conn_id, "vlan_id": vlan_id})

    def create_vlan_port(self, machine_id: str, conn_id: str, vlan_id: int, data: Dict[str, Any]) -> APIResponse:
        """Create a vlan port forwarder and return response."""
        return self._post("vlan_port_list", {"pk": self.user_pk, "sdi_id": self.sdi_pk, "machine_id": machine_id, "connection_id": conn_id, "vlan_id": vlan_id}, data)

    def get_vlan_port(self, machine_id: str, conn_id: str, vlan_id: int, port_id: int) -> APIResponse:
        """Get vlan port forwarder and return response."""
        return self._get("vlan_port_detail", {"pk": self.user_pk, "sdi_id": self.sdi_pk, "machine_id": machine_id, "connection_id": conn_id, "vlan_id": vlan_id, "port_id": port_id})

    def delete_vlan_port(self, machine_id: str, conn_id: str, vlan_id: int, port_id: int) -> APIResponse:
        """Delete vlan port forwarder and return response."""
        return self._delete("vlan_port_detail", {"pk": self.user_pk, "sdi_id": self.sdi_pk, "machine_id": machine_id, "connection_id": conn_id, "vlan_id": vlan_id, "port_id": port_id})
