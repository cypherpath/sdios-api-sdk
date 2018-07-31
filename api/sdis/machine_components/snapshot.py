"""SnapshotDriver class object"""
from typing import Any, Dict, Optional

from api.sdis.machine_components.base_machine import BaseMachine
from api.driver import APIDriver
from api.driver import APIResponse
from settings.urls import APICategory


class SnapshotDriver(BaseMachine):
    """Make all machine snapshot API calls."""
    _category = APICategory.MACHINE_SNAPSHOTS

    def __init__(self, api_driver: APIDriver) -> None:
        """Initialize SnapshotDriver class

        :param api_driver: Allows the driver to communicate with SDI OS
        :type api_driver: APIDriver class object
        """
        super().__init__(api_driver)

    def get_snapshots(self, machine_id: str) -> APIResponse:
        """Get all machine snapshots and return response."""
        return self._get("list", {"pk": self.user_pk, "sdi_id": self.sdi_pk, "machine_id": machine_id})

    def is_snapshot(self, machine_id: str, snap_tag: str) -> Optional[bool]:
        """Check if snapshot tag is saved on the machine and return boolean."""
        response = self.get_snapshots(machine_id)
        if response.ok:
            snap_list = response.detail
            return any(snap_tag in value["tag"] for value in snap_list)
        return None

    def create_snapshot(self, machine_id: str, data: Dict[str, Any]) -> APIResponse:
        """Create a machine snapshot and return response."""
        return self._post("list", {"pk": self.user_pk, "sdi_id": self.sdi_pk, "machine_id": machine_id}, data)

    def get_snapshot(self, machine_id: str, tag: str) -> APIResponse:
        """Get details of machine snapshot and return response."""
        return self._get("detail", {"pk": self.user_pk, "sdi_id": self.sdi_pk, "machine_id": machine_id, "snap_tag": tag})

    def apply_snapshot(self, machine_id: str, tag: str) -> APIResponse:
        """Apply machine snapshot and return response."""
        return self._put("detail", {"pk": self.user_pk, "sdi_id": self.sdi_pk, "machine_id": machine_id, "snap_tag": tag})
