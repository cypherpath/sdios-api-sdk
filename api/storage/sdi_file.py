"""SDIFileDriver class object"""
from typing import Any, Dict, Optional

from api.base_driver import BaseDriver
from api.driver import APIDriver
from api.driver import APIResponse
from settings.urls import APICategory


class SDIFileDriver(BaseDriver):
    """Make all SDI files API calls."""
    _category = APICategory.SDI_FILES

    def __init__(self, api_driver: APIDriver) -> None:
        """Initialize SDIFileDriver class

        :param api_driver: Allows SDIFileDriver to communicate with SDI OS
        :type api_driver: APIDriver class object
        """
        super().__init__(api_driver)
        self.user_pk = None # type: Optional[int]

    def clear(self) -> None:
        """Clear pks."""
        self.user_pk = None # type: Optional[int]

    def get_all(self) -> APIResponse:
        """Get all SDI files on SDI OS and return response."""
        return self._get("list")

    def get_sdi_files(self) -> APIResponse:
        """Get user's SDI files and return response."""
        return self._get("user_list", {"pk": self.user_pk})

    def get_sdi_file(self, file_key: str) -> APIResponse:
        """Get SDI files details and return response."""
        return self._get("file_detail", {"pk": self.user_pk, "file_key": file_key})

    def find_file_key(self, sdi_file_name: str) -> Optional[str]:
        """Find SDI file key in users" SDI file store by SDI file name and return key.

        If key is not found, return None.
        """
        response = self.get_sdi_files()
        if response.ok:
            for sdi_file in response.detail["files"]:
                if sdi_file_name == sdi_file["name"]:
                    return sdi_file["key"]
        else:
            print("Error finding file key:")
            print(response)
        return None

    def delete_sdi_file(self, file_key: str) -> APIResponse:
        """Delete SDI files and return response."""
        return self._delete("file_detail", {"pk": self.user_pk, "file_key": file_key})

    def import_sdi_file(self, file_key: str, data: Dict[str, Any]) -> APIResponse:
        """Import SDI files and return response."""
        return self._put("import", {"pk": self.user_pk, "file_key": file_key}, data)

    def get_uploads(self) -> APIResponse:
        """Get user's SDI files uploads."""
        return self._get("upload_list", {"pk": self.user_pk})

    def start_upload(self, data: Dict[str, Any]) -> APIResponse:
        """Start a SDI files upload and return response."""
        return self._post("upload_list", {"pk": self.user_pk}, data)

    def get_upload(self, key: int) -> APIResponse:
        """Get details of an upload and return response."""
        return self._get("upload_detail", {"pk": self.user_pk, "file_upload_key": key})

    def upload_chunk(self, key: int, chunk: Dict[str, Any]) -> APIResponse:
        """"Send a chunk of the SDI files and return response."""
        return self._put("upload_detail", {"pk": self.user_pk, "file_upload_key": key}, files=chunk)

    def finish_upload(self, key: int) -> APIResponse:
        """When a SDI files upload has finished, send the EOF and return response."""
        eof_data = {"eof": True}
        return self._put("upload_detail", {"pk": self.user_pk, "file_upload_key": key}, data=eof_data)

    def delete_upload(self, key: int) -> APIResponse:
        """Delete a started upload and return response."""
        return self._delete("upload_detail", {"pk": self.user_pk, "file_upload_key": key})
