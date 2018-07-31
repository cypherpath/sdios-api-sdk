"""GeneralDriver class object"""
from typing import Any, Dict, Optional

from api.base_driver import BaseDriver
from api.driver import APIDriver
from api.driver import APIResponse
from settings.urls import APICategory


class GeneralDriver(BaseDriver):
    """Make all general storage API calls."""
    _category = APICategory.GENERAL

    def __init__(self, api_driver: APIDriver) -> None:
        """Initialize GeneralDriver class

        :param api_driver: Allows GeneralDriver to communicate with SDI OS
        :type api_driver: APIDriver class object
        """
        super().__init__(api_driver)
        self.user_pk = None # type: Optional[int]

    def clear(self) -> None:
        """Clear pks."""
        self.user_pk = None # type: Optional[int]

    def get_all(self) -> APIResponse:
        """Get general storage for all users on SDI OS and return response."""
        return self._get("list")

    def get_storage(self) -> APIResponse:
        """Get user's general storage and return response."""
        return self._get("user_list", {"pk": self.user_pk})

    def create_in_root(self, data: Dict[str, Any]) -> APIResponse:
        """Create a directory in root and return response."""
        return self._post("user_list", {"pk": self.user_pk}, data)

    def get_in_dir(self, dir_key: str) -> APIResponse:
        """Get contents from a specific directory and return response."""
        return self._get("directory_list", {"pk": self.user_pk, "directory_key": dir_key})

    def get_dir_path(self, dir_key: str) -> Optional[str]:
        """Return the full directory path with a given directory key."""
        response = self.get_in_dir(dir_key)
        if response.ok:
            return response.detail["directory"][1:]
        return None

    def create_in_dir(self, dir_key: str, data: Dict[str, Any]) -> APIResponse:
        """Create a directory in a specific directory and return response."""
        return self._post("directory_list", {"pk": self.user_pk, "dirctory_key": dir_key}, data)

    def delete_dir(self, dir_key: str) -> APIResponse:
        """Delete directory and all contents and return response."""
        return self._delete("directory_list", {"pk": self.user_pk, "directory_key": dir_key})

    def get_file(self, file_key: str) -> APIResponse:
        """Get details of file and return response."""
        return self._get("file_details", {"pk": self.user_pk, "file_key": file_key})

    def delete_file(self, file_key: str) -> APIResponse:
        """Delete file and return response."""
        return self._delete("file_details", {"pk": self.user_pk, "file_key": file_key})

    def move_file(self, file_key: str, data: Dict[str, Any]) -> APIResponse:
        """Move a file to a different directory and return response."""
        return self._put("file_move", {"pk": self.user_pk, "file_key": file_key}, data)

    def get_uploads(self) -> APIResponse:
        """Get general storage uploads and return response."""
        return self._get("upload_list", {"pk": self.user_pk})

    def start_upload(self, data: Dict[str, Any]) -> APIResponse:
        """Start a general storage upload and return response."""
        return self._post("upload_list", {"pk": self.user_pk}, data)

    def get_upload(self, key: int) -> APIResponse:
        """Get details of an upload and return response."""
        return self._get("upload_details", {"pk": self.user_pk, "general_upload_key": key})

    def upload_chunk(self, key: int, chunk: Dict[str, Any]) -> APIResponse:
        """Send a chunk of the file and return response."""
        return self._put("upload_details", {"pk": self.user_pk, "general_upload_key": key}, files=chunk)

    def finish_upload(self, key: int) -> APIResponse:
        """When a file is finished uploading, send the EOF and return response."""
        eof_data = {"eof": True}
        return self._put("upload_details", {"pk": self.user_pk, "general_upload_key": key}, data=eof_data)

    def delete_upload(self, key: int) -> APIResponse:
        """Delete a started upload and return response."""
        return self._delete("upload_details", {"pk": self.user_pk, "general_upload_key": key})
