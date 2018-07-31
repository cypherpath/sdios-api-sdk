"""NetworkDriver class object"""
from typing import Any, Dict, Optional

from api.base_driver import BaseDriver
from api.driver import APIDriver
from api.driver import APIResponse
from settings.urls import APICategory


class NetworkDriver(BaseDriver):
    """Make all network API calls."""
    _category = APICategory.NETWORKS

    def __init__(self, api_driver: APIDriver) -> None:
        """Initialize NetworkDriver class

        :param api_driver: Allows NetworkDriver to communicate with SDI OS
        :type api_driver: APIDriver class object
        """
        super().__init__(api_driver)
        self.sdi_pk = None # type: Optional[str]
        self.user_pk = None # type: Optional[int]

    def clear(self) -> None:
        """Clear pks."""
        self.sdi_pk = None # type: Optional[str]
        self.user_pk = None # type: Optional[int]

    def create(self, data: Dict[str, Any], user_pk: int = None, sdi_pk: str = None) -> APIResponse:
        """Create network and return response."""
        url_args = {"pk": self.user_pk if user_pk is None else user_pk,
                    "sdi_id": self.sdi_pk if sdi_pk is None else sdi_pk}
        return self._post("list", url_args, data)

    def get_network(self, network_id: str) -> APIResponse:
        """Get network details and return response."""
        return self._get("detail", {"pk": self.user_pk, "sdi_id": self.sdi_pk, "network_id": network_id})

    def modify(self, network_id: str, data: Dict[str, Any], user_pk: int = None, sdi_pk: str = None) -> APIResponse:
        """Modify a network and return response."""
        url_args = {"pk": self.user_pk if user_pk is None else user_pk,
                    "sdi_id": self.sdi_pk if sdi_pk is None else sdi_pk,
                    "network_id": network_id}
        return self._put("detail", url_args, data)

    def replug(self, network_id: str, data: Dict[str, Any]) -> APIResponse:
        """Send replug request to network and return response."""
        return self._put("replug", {"pk": self.user_pk, "sdi_id": self.sdi_pk, "network_id": network_id}, data)

    def delete(self, network_id: str) -> APIResponse:
        """Delete a network and return response."""
        return self._delete("detail", {"pk": self.user_pk, "sdi_id": self.sdi_pk, "network_id": network_id})

    def get_all_networks(self, user_pk: int = None, sdi_pk: str = None) -> APIResponse:
        """Get all networks in a sdi and return response."""
        url_args = {"pk": self.user_pk if user_pk is None else user_pk,
                    "sdi_id": self.sdi_pk if sdi_pk is None else sdi_pk}
        return self._get("list", url_args)

    def get_all_services(self, network_id: str) -> APIResponse:
        """Get network's services and return response."""
        return self._get("service_list", {"pk": self.user_pk, "sdi_id": self.sdi_pk, "network_id": network_id})

    def create_service(self, network_id: str, data: Dict[str, Any]) -> APIResponse:
        """Create service for network and return response."""
        return self._post("service_list", {"pk": self.user_pk, "sdi_id": self.sdi_pk, "network_id": network_id}, data)

    def get_service(self, network_id: str, service_id: int) -> APIResponse:
        """Get network's service details and return response."""
        return self._get("service_detail", {"pk": self.user_pk, "sdi_id": self.sdi_pk, "network_id": network_id, "service_id": service_id})

    def modify_service(self, network_id: str, service_id: int, data: Dict[str, Any]) -> APIResponse:
        """Modify network's service and return response."""
        return self._put("service_detail", {"pk": self.user_pk, "sdi_id": self.sdi_pk, "network_id": network_id, "service_id": service_id}, data)

    def delete_service(self, network_id: str, service_id: int) -> APIResponse:
        """Delete network's service and return response."""
        return self._delete("service_detail", {"pk": self.user_pk, "sdi_id": self.sdi_pk, "network_id": network_id, "service_id": service_id})

    def get_dhcp_pools(self, network_id: str, service_id: int) -> APIResponse:
        """Get all DHCP pools for network and return response."""
        return self._get("pool_list", {"pk": self.user_pk, "sdi_id": self.sdi_pk, "network_id": network_id, "service_id": service_id})

    def create_dhcp_pool(self, network_id: str, service_id: int, data: Dict[str, Any]) -> APIResponse:
        """Create dhcp pool for network and return response."""
        return self._post("pool_list", {"pk": self.user_pk, "sdi_id": self.sdi_pk, "network_id": network_id, "service_id": service_id}, data)

    def get_dhcp_pool(self, network_id: str, service_id: int, pool_id: str) -> APIResponse:
        """Get details of network's dhcp pool and return response."""
        return self._get("pool_detail", {"pk": self.user_pk, "sdi_id": self.sdi_pk, "network_id": network_id, "service_id": service_id, "pool_id": pool_id})

    def modify_dhcp_pool(self, network_id: str, service_id: int, pool_id: str, data: Dict[str, Any]) -> APIResponse:
        """Modify network's dhcp pool and return response."""
        return self._put("pool_detail", {"pk": self.user_pk, "sdi_id": self.sdi_pk, "network_id": network_id, "service_id": service_id, "pool_id": pool_id}, data)

    def delete_dhcp_pool(self, network_id: str, service_id: int, pool_id: str) -> APIResponse:
        """Delete network's dhcp pool and return response."""
        return self._delete("pool_detail", {"pk": self.user_pk, "sdi_id": self.sdi_pk, "network_id": network_id, "service_id": service_id, "pool_id": pool_id})
