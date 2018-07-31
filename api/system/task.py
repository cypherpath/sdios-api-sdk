"""TaskDriver class object"""
from typing import Dict, List

from api.base_driver import BaseDriver
from api.driver import APIDriver
from api.driver import APIResponse
from settings.urls import APICategory


class TaskDriver(BaseDriver):
    """Make all system task API calls."""
    _category = APICategory.SYSTEM_TASKS

    def __init__(self, api_driver: APIDriver) -> None:
        """Initialize SystemDriver class

        :param api_driver: Allows SystemDriver to communicate with SDI OS
        :type api_driver: APIDriver class object
        """
        super().__init__(api_driver)

    def get_all_tasks(self) -> APIResponse:
        """Get all long running processes running and return response."""
        return self._get("system_list")

    def get_user_tasks(self, user_pk: int) -> APIResponse:
        """Get long running processes for given user and return response."""
        user_args = {"pk": user_pk}
        return self._get("user_list", user_args)

    def get_task(self, lrpid: str, user_pk: int = None) -> APIResponse:
        """Get details on a user's long running process task and return response."""
        url_args = {"lrpid": lrpid, "pk": user_pk} if user_pk is not None else {"lrpid": lrpid}
        return self._get("user_detail", url_args)

    def cancel_task(self, lrpid: str, user_pk: int = None) -> APIResponse:
        """Cancel a user's long running process task and return response."""
        url_args = {"lrpid": lrpid, "pk": user_pk} if user_pk is not None else {"lrpid": lrpid}
        return self._delete("user_detail", url_args)

    def reorder_tasks(self, data: Dict[str, List[str]]) -> APIResponse:
        """Reorder pending tasks and return response.

        If the following set of pending tasks exist: [‘a’, ‘b’, ‘c’, ‘d’].
        And the desired order is: [‘a’, ‘c’, ‘b’, ‘d’].
        Submit the following to reorder the two tasks: [‘c’, ‘b’]
        e.g. {"order": ["c", "b"]}
        """
        return self._post("reorder", data=data)
