"""DiskDriver class object"""
from typing import Any, Dict, List, Optional

from api.base_driver import BaseDriver
from api.driver import APIDriver
from api.driver import APIResponse
from settings.urls import APICategory


class DiskDriver(BaseDriver):
    """Make all disk image API calls."""
    _category = APICategory.DISKS

    def __init__(self, api_driver: APIDriver) -> None:
        """Initialize DiskDriver class

        :param api_driver: Allows DiskDriver to communicate with SDI OS
        :type api_driver: APIDriver class object
        """
        super().__init__(api_driver)
        self.user_pk = None # type: Optional[int]

    def clear(self) -> None:
        """Clear pks."""
        self.user_pk = None # type: Optional[int]

    def create(self, data: Dict[str, Any]) -> APIResponse:
        """Create blank disk in user_pk in passed data argument and return response."""
        return self._post("list", data=data)

    def user_create(self, data: Dict[str, Any]) -> APIResponse:
        """Create blank disk in user's disk store and return response."""
        return self._post("user_list", {"pk": self.user_pk}, data)

    def get_uploads(self) -> APIResponse:
        """Get user's disk uploads."""
        return self._get("upload_list", {"pk": self.user_pk})

    def start_upload(self, data: Dict[str, Any]) -> APIResponse:
        """Start a disk upload and return response."""
        return self._put("upload_list", {"pk": self.user_pk}, data)

    def get_upload(self, key: int) -> APIResponse:
        """Get details of an upload and return response."""
        return self._get("upload_detail", {"pk": self.user_pk, "disk_upload_key": key})

    def upload_chunk(self, key: int, chunk: Dict[str, Any]) -> APIResponse:
        """Send a chunk of the disk and return response."""
        return self._put("upload_detail", {"pk": self.user_pk, "disk_upload_key": key}, files=chunk)

    def finish_upload(self, key: int) -> APIResponse:
        """When a disk upload has finished, send the EOF and return response."""
        eof_data = {"eof": True}
        return self._put("upload_detail", {"pk": self.user_pk, "disk_upload_key": key}, data=eof_data)

    def delete_upload(self, key: int) -> APIResponse:
        """Delete an ongoing upload and return response."""
        return self._delete("upload_detail", {"pk": self.user_pk, "disk_upload_key": key})

    def get_all(self) -> APIResponse:
        """Get all disks in SDI OS and return response."""
        return self._get("list")

    def get_disks(self) -> APIResponse:
        """Get users disks and return response."""
        return self._get("user_list", {"pk": self.user_pk})

    def get_disk(self, image_id: str) -> APIResponse:
        """Get a user's disk information and return response."""
        return self._get("user_detail", {"pk": self.user_pk, "image_id": image_id})

    def get_users_disk_id(self, disk_name: str) -> Optional[str]:
        """Search through user's disk store and return uuid of matching disk name."""
        response = self.get_disks()
        if response.ok:
            return self.__search_disks(disk_name, response.detail)
        return None

    def get_disk_id(self, disk_name: str) -> Optional[str]:
        """Search all disks on deployment and return uuid of matching disk name."""
        response = self.get_all()
        if response.ok:
            return self.__search_disks(disk_name, response.detail)
        return None

    @staticmethod
    def __search_disks(disk_name: str, disk_list: List[Dict[str, Any]]) -> Optional[str]:
        for uuid in disk_list:
            if disk_name == uuid["name"]:
                return uuid["image_id"]
        return None

    def is_pending(self, image_id: str) -> Optional[bool]:
        """Check if disk is in a pending state and return response."""
        response = self.get_disk(image_id)
        if response.ok:
            return response.detail["pending"]
        return None

    def modify_disk(self, image_id: str, data: Dict[str, Any]) -> APIResponse:
        """Modify disk and return response."""
        return self._put("user_detail", {"pk": self.user_pk, "image_id": image_id}, data)

    def delete_disk(self, image_id: str) -> APIResponse:
        """Delete disk and return response."""
        return self._delete("user_detail", {"pk": self.user_pk, "image_id": image_id})

    def copy(self, image_id: str, data: Dict[str, Any]) -> APIResponse:
        """Copy disk and return response."""
        return self._post("copy", {"pk": self.user_pk, "image_id": image_id}, data)

    def get_permissions(self, image_id: str) -> APIResponse:
        """Get a disk's permissions and return response."""
        return self._get("permissions", {"pk": self.user_pk, "image_id": image_id})

    def modify_permissions(self, image_id: str, data: Dict[str, Any]) -> APIResponse:
        """Modify a disk's permissions and return response."""
        return self._put("permissions", {"pk": self.user_pk, "image_id": image_id}, data)
