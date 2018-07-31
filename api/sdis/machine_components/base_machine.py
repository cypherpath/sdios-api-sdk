"""Machine base class object"""
from typing import Optional

from api.base_driver import BaseDriver
from api.driver import APIDriver


class BaseMachine(BaseDriver):
    """Parent class for all machine drivers."""

    def __init__(self, api_driver: APIDriver) -> None:
        """Initialize MachineDriver class

        :param api_driver: Allows the driver to communicate with SDI OS
        :type api_driver: APIDriver class object
        """
        super().__init__(api_driver)
        self.__sdi_pk = None # type: Optional[str]
        self.__user_pk = None # type: Optional[int]

    @property
    def sdi_pk(self) -> Optional[str]:
        """String to store SDI's pk used for machine calls"""
        return self.__sdi_pk

    @sdi_pk.setter
    def sdi_pk(self, sdi_pk: str) -> None:
        self.__sdi_pk = sdi_pk

    @property
    def user_pk(self) -> Optional[int]:
        """String to store user's pk used for machine calls"""
        return self.__user_pk

    @user_pk.setter
    def user_pk(self, user_pk: int) -> None:
        self.__user_pk = user_pk

    def clear(self) -> None:
        """Clear pks."""
        self.sdi_pk = None # type: Optional[str]
        self.user_pk = None # type: Optional[int]
