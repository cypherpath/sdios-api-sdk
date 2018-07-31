"""SDIDriver class object"""
from typing import Any, Dict, Optional

from api.base_driver import BaseDriver
from api.driver import APIDriver
from api.driver import APIResponse
from settings.urls import APICategory


class SDIDriver(BaseDriver):
    """Make all sdi API calls."""
    _category = APICategory.SDIS

    def __init__(self, api_driver: APIDriver) -> None:
        """Initialize SDIDriver class object

        :param api_driver: Allows SDIDriver to communicate with SDI OS
        :type api_driver: APIDriver class object
        """
        super().__init__(api_driver)
        self.user_pk = None # type: Optional[int]

    def clear(self) -> None:
        """Clear pks."""
        self.user_pk = None # type: Optional[int]

    def create(self, data: Dict[str, Any], user_pk: int = None) -> APIResponse:
        """Create a sdi and return response."""
        url_args = {"pk": self.user_pk if user_pk is None else user_pk}
        return self._post("user_list", url_args, data)

    def get_all_sdis(self) -> APIResponse:
        """Get all sdis in the deployment and return response."""
        return self._get("list")

    def get_users_sdis(self, user_pk: int = None) -> APIResponse:
        """Get user's sdis and return response."""
        url_args = {"pk": self.user_pk if user_pk is None else user_pk}
        return self._get("user_list", url_args)

    def get(self, sdi_id: str) -> APIResponse:
        """Get sdi's details and return response."""
        return self._get("user_detail", {"pk": self.user_pk, "sdi_id": sdi_id})

    def modify(self, sdi_id: str, data: Dict[str, Any]) -> APIResponse:
        """Modify a sdi and return response."""
        return self._put("user_detail", {"pk": self.user_pk, "sdi_id": sdi_id}, data)

    def delete(self, sdi_id: str) -> APIResponse:
        """Delete sdi and return response."""
        return self._delete("user_detail", {"pk": self.user_pk, "sdi_id": sdi_id})

    def copy(self, sdi_id: str, data: Dict[str, Any]) -> APIResponse:
        """Copy a sdi and return response."""
        return self._post("copy", {"pk": self.user_pk, "sdi_id": sdi_id}, data)

    def is_copying(self, sdi_id: str) -> bool:
        """Check if sdi's status is copying and return boolean."""
        raise NotImplementedError

    def export(self, sdi_id: str) -> APIResponse:
        """Export a sdi and return response."""
        return self._post("export", {"pk": self.user_pk, "sdi_id": sdi_id})

    def is_exporting(self, sdi_id: str) -> Optional[bool]:
        """Check if sdi's status is exporting and return boolean."""
        response = self.get_status(sdi_id)
        if response.ok:
            return response.detail["export_progress"] is not None
        return None

    def get_permissions(self, sdi_id: str) -> APIResponse:
        """Get a sdi's permissions and return response."""
        return self._get("permissions", {"pk": self.user_pk, "sdi_id": sdi_id})

    def modify_permissions(self, sdi_id: str, data: Dict[str, Any]) -> APIResponse:
        """Modify a sdi's permissions and return response."""
        return self._put("permissions", {"pk": self.user_pk, "sdi_id": sdi_id}, data)

    def start(self, sdi_id: str) -> APIResponse:
        """Start a sdi and return response."""
        return self._post("start", {"pk": self.user_pk, "sdi_id": sdi_id})

    def is_starting(self, sdi_id: str) -> Optional[bool]:
        """Check if sdi's status is starting and return boolean."""
        response = self.get_status(sdi_id)
        if response.ok:
            return str(response.detail["state"]) == "1"
        return None

    def is_running(self, sdi_id: str) -> Optional[bool]:
        """Check if sdi's status is running and return boolean."""
        response = self.get_status(sdi_id)
        if response.ok:
            return str(response.detail["state"]) == "2"
        return None

    def stop(self, sdi_id: str) -> APIResponse:
        """Stop a sdi and return response."""
        return self._post("stop", {"pk": self.user_pk, "sdi_id": sdi_id})

    def is_stopping(self, sdi_id: str) -> Optional[bool]:
        """Check if sdi's status is stopping and return boolean."""
        response = self.get_status(sdi_id)
        if response.ok:
            return str(response.detail["state"]) == "3"
        return None

    def is_stopped(self, sdi_id: str) -> Optional[bool]:
        """Check if sdi's status is stopped and return boolean."""
        response = self.get_status(sdi_id)
        if response.ok:
            return str(response.detail["state"]) == "0"
        return None

    def get_settings(self, sdi_id: str) -> APIResponse:
        """Get a sdi's settings and return response."""
        return self._get("settings", {"pk": self.user_pk, "sdi_id": sdi_id})

    def modify_settings(self, sdi_id: str, data: Dict[str, Any]) -> APIResponse:
        """Modify a sdi's settings and return response."""
        return self._put("settings", {"pk": self.user_pk, "sdi_id": sdi_id}, data)

    def get_all_checkpoints(self, sdi_id: str) -> APIResponse:
        """Get all checkpoints and return response."""
        return self._get("checkpoint", {"pk": self.user_pk, "sdi_id": sdi_id})

    def is_checkpoint(self, sdi_id: str, check_tag: str) -> Optional[bool]:
        """Check if checkpoint tag is in sdi and return boolean."""
        response = self.get_all_checkpoints(sdi_id)
        if response.ok:
            check_list = response.detail
            return any(check_tag in value["tag"] for value in check_list)
        return None

    def create_checkpoint(self, sdi_id: str, data: Dict[str, Any]) -> APIResponse:
        """Create a sdi checkpoint and return response."""
        return self._post("checkpoint", {"pk": self.user_pk, "sdi_id": sdi_id}, data)

    def get_checkpoint(self, sdi_id: str, check_tag: str) -> APIResponse:
        """Get a checkpoint's details and return response."""
        return self._get("checkpoint_detail", {"pk": self.user_pk, "sdi_id": sdi_id, "check_tag": check_tag})

    def load_checkpoint(self, sdi_id: str, check_tag: str) -> APIResponse:
        """Load a checkpoint and return response."""
        return self._put("checkpoint_detail", {"pk": self.user_pk, "sdi_id": sdi_id, "check_tag": check_tag})

    def delete_checkpoint(self, sdi_id: str, check_tag: str) -> APIResponse:
        """Delete a checkpoint and return response."""
        return self._delete("checkpoint_detail", {"pk": self.user_pk, "sdi_id": sdi_id, "check_tag": check_tag})

    def get_ports(self, sdi_id: str) -> APIResponse:
        """Get a sdi's ports and return response."""
        return self._get("port_list", {"pk": self.user_pk, "sdi_id": sdi_id})

    def create_port(self, sdi_id: str, data: Dict[str, Any]) -> APIResponse:
        """Create a port and return a response."""
        return self._post("port_list", {"pk": self.user_pk, "sdi_id": sdi_id}, data)

    def get_history(self, sdi_id: str) -> APIResponse:
        """Get a sdi's history and return response."""
        return self._get("history", {"pk": self.user_pk, "sdi_id": sdi_id})

    def get_status(self, sdi_id: str) -> APIResponse:
        """Get a sdi's status and return response."""
        return self._get("status", {"pk": self.user_pk, "sdi_id": sdi_id})

    def get_persistence(self, sdi_id: str) -> APIResponse:
        """Get sdi's persistence details and return response."""
        return self._get("persist", {"pk": self.user_pk, "sdi_id": sdi_id})

    def modify_persistence(self, sdi_id: str, data: Dict[str, Any]) -> APIResponse:
        """Modify sdi's persistence details and return response."""
        return self._put("persist", {"pk": self.user_pk, "sdi_id": sdi_id}, data)

    def get_overview(self, sdi_id: str) -> APIResponse:
        """Get a sdi's overview and return response."""
        return self._get("overview", {"pk": self.user_pk, "sdi_id": sdi_id})
