"""MachineDriver class object"""
from typing import Any, Dict, Optional

from api.base_driver import BaseDriver
from api.sdis.machine_components import BaseMachine, DriveDriver, InterfaceDriver, RoutingDriver, SnapshotDriver
from api.driver import APIDriver
from api.driver import APIResponse
from settings.urls import APICategory


class MachineDriver(BaseMachine):
    """Make all machine API calls."""
    _category = APICategory.MACHINES

    def __init__(self, api_driver: APIDriver) -> None:
        """Initialize MachineDriver class

        :param api_driver: Allows MachineDriver to communicate with SDI OS
        :type api_driver: APIDriver class object
        """
        super().__init__(api_driver)
        self.__interface_driver = InterfaceDriver(api_driver)
        self.__drive_driver = DriveDriver(api_driver)
        self.__routing_driver = RoutingDriver(api_driver)
        self.__snapshot_driver = SnapshotDriver(api_driver)

    @property
    def sdi_pk(self) -> Optional[str]:
        """String to store SDI's pk used for machine calls"""
        return self.__sdi_pk

    @sdi_pk.setter
    def sdi_pk(self, sdi_pk: str) -> None:
        self.__sdi_pk = sdi_pk
        self.__interface_driver.sdi_pk = sdi_pk
        self.__routing_driver.sdi_pk = sdi_pk
        self.__snapshot_driver.sdi_pk = sdi_pk

    @property
    def user_pk(self) -> Optional[int]:
        """String to store user's pk used for machine calls"""
        return self.__user_pk

    @user_pk.setter
    def user_pk(self, user_pk: int) -> None:
        self.__user_pk = user_pk
        self.__interface_driver.user_pk = user_pk
        self.__routing_driver.user_pk = user_pk
        self.__snapshot_driver.user_pk = user_pk

    @property
    def interface(self) -> InterfaceDriver:
        """Interface driver object used to make calls specific to machine interfaces"""
        return self.__interface_driver

    @property
    def drive(self) -> DriveDriver:
        """Drive driver object used to make calls specific to machine drives"""
        return self.__drive_driver

    @property
    def routing(self) -> RoutingDriver:
        """Router driver object used to make calls specific to machine routing"""
        return self.__routing_driver

    @property
    def snapshot(self) -> SnapshotDriver:
        """Snapshot driver object used to make calls specific to machine snapshots"""
        return self.__snapshot_driver

    def create(self, data: Dict[str, Any]) -> APIResponse:
        """Create machine and return response."""
        return self._post("list", {"pk": self.user_pk, "sdi_id": self.sdi_pk}, data)

    def get_all(self) -> APIResponse:
        """Get all machines in the sdi and return response."""
        return self._get("list", {"pk": self.user_pk, "sdi_id": self.sdi_pk})

    def get_machine(self, machine_id: str) -> APIResponse:
        """Get machine details and return response."""
        return self._get("detail", {"pk": self.user_pk, "sdi_id": self.sdi_pk, "machine_id": machine_id})

    def modify(self, machine_id: str, data: Dict[str, Any]) -> APIResponse:
        """Modify a machine and return response."""
        return self._put("detail", {"pk": self.user_pk, "sdi_id": self.sdi_pk, "machine_id": machine_id}, data)

    def delete(self, machine_id: str) -> APIResponse:
        """Delete a machine and return response."""
        return self._delete("detail", {"pk": self.user_pk, "sdi_id": self.sdi_pk, "machine_id": machine_id})

    def get_vnc(self, machine_id: str) -> APIResponse:
        """Get machine's vnc data and return response."""
        return self._get("vnc", {"pk": self.user_pk, "sdi_id": self.sdi_pk, "machine_id": machine_id})

    def get_status(self, machine_id: str) -> APIResponse:
        """Get machine's status and return response."""
        return self._get("status", {"pk": self.user_pk, "sdi_id": self.sdi_pk, "machine_id": machine_id})

    def start(self, machine_id: str) -> APIResponse:
        """Start machine and return response."""
        return self._put("start", {"pk": self.user_pk, "sdi_id": self.sdi_pk, "machine_id": machine_id})

    def is_running(self, machine_id: str) -> Optional[bool]:
        """Check if machine's status is running and return boolean."""
        response = self.get_status(machine_id)
        if response.ok:
            try:
                return False if response.reason == "No Content" else response.detail["running"]
            except TypeError as err:
                print(err)
                print("Response:", response)
        else:
            print("Failed to check if machine is running")
            print(response)
        return None

    def is_machines_running(self) -> Optional[bool]:
        """Check if all machines in sdi are running and return boolean."""
        all_running = None
        response = self.get_all()
        if response.ok:
            all_running = True
            machines_list = response.detail["user"] + response.detail["managed"]
            for machine in machines_list:
                running = self.is_running(machine["id"])
                if not running:
                    all_running = False
        return all_running

    def kill(self, machine_id: str) -> APIResponse:
        """Stop machine and return response."""
        return self._put("stop", {"pk": self.user_pk, "sdi_id": self.sdi_pk, "machine_id": machine_id})

    def acpi(self, machine_id: str) -> APIResponse:
        """Send ACPI shutdown to machine and return response."""
        return self._put("power_off", {"pk": self.user_pk, "sdi_id": self.sdi_pk, "machine_id": machine_id})

    def resume(self, machine_id: str) -> APIResponse:
        """Resume machine and return response."""
        return self._put("resume", {"pk": self.user_pk, "sdi_id": self.sdi_pk, "machine_id": machine_id})

    def suspend(self, machine_id: str) -> APIResponse:
        """Suspend machine and return response."""
        return self._put("suspend", {"pk": self.user_pk, "sdi_id": self.sdi_pk, "machine_id": machine_id})
