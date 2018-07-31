"""InterfaceDriver class object"""
from typing import Any, Dict, List

from api.sdis.machine_components.base_machine import BaseMachine
from api.driver import APIDriver
from api.driver import APIResponse
from settings.urls import APICategory


class DriveDriver(BaseMachine):
    """Make all machine drive API calls."""
    _category = APICategory.MACHINE_DRIVES

    def __init__(self, api_driver: APIDriver) -> None:
        """Initialize InterfaceDriver class

        :param api_driver: Allows the driver to communicate with SDI OS
        :type api_driver: APIDriver class object
        """
        super().__init__(api_driver)

    def get_drives(self, machine_id: str) -> APIResponse:
        """Get machine's drives and return a response."""
        return self._get("list", {"pk": self.user_pk, "sdi_id": self.sdi_pk, "machine_id": machine_id})

    def delete_drive(self, machine_id: str, slot: int) -> APIResponse:
        """Remove machine's drive in given slot and return a response."""
        return self._delete("detail", {"pk": self.user_pk, "sdi_id": self.sdi_pk, "machine_id": machine_id, "disk_slot": slot})

    def add_drive(self, machine_id: str, data: Dict[str, Any]) -> APIResponse:
        """Add a drive to a machine and return a response."""
        return self._post("list", {"pk": self.user_pk, "sdi_id": self.sdi_pk, "machine_id": machine_id}, data)

    def get_drive_order(self, machine_id: str) -> APIResponse:
        """Get machine drive's order and return response."""
        return self._get("order", {"pk": self.user_pk, "sdi_id": self.sdi_pk, "machine_id": machine_id})

    def modify_drive_order(self, machine_id: str, data: Dict[str, List[int]]) -> APIResponse:
        """Modify machine drive's order and return response."""
        return self._put("order", {"pk": self.user_pk, "sdi_id": self.sdi_pk, "machine_id": machine_id}, data)

    def get_drive(self, machine_id: str, slot: int) -> APIResponse:
        """Get info for disk in given slot and return response."""
        return self._get("detail", {"pk": self.user_pk, "sdi_id": self.sdi_pk, "machine_id": machine_id, "disk_slot": slot})

    def modify_drive(self, machine_id: str, slot: int, data: Dict[str, Any]) -> APIResponse:
        """Modify machine drive and return response."""
        return self._put("detail", {"pk": self.user_pk, "sdi_id": self.sdi_pk, "machine_id": machine_id, "disk_slot": slot}, data)

    def save_new_master(self, machine_id: str, slot: int) -> APIResponse:
        """Save a new master for disk and return response."""
        return self._put("save_new", {"pk": self.user_pk, "sdi_id": self.sdi_pk, "machine_id": machine_id, "disk_slot": slot})

    def save_master(self, machine_id: str, slot: int) -> APIResponse:
        """Save to master for disk and return response."""
        return self._put("save_base", {"pk": self.user_pk, "sdi_id": self.sdi_pk, "machine_id": machine_id, "disk_slot": slot})
