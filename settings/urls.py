"""API URLs"""
from typing import Any, Dict

from enum import Enum

CURRENT_API_VER = "2.1.0"

class APICategory(Enum):
    AUTHENTICATION = "authentication"
    USERS = "users"
    GROUPS = "groups"
    TENANCIES = "tenancies"
    SYSTEM_SETTINGS = "system settings"
    SYSTEM_STATUS = "system status"
    SYSTEM_TASKS = "system tasks"
    DISKS = "disks"
    GENERAL = "general"
    SDI_FILES = "SDI files"
    SDIS = "SDIs"
    MACHINES = "machines"
    MACHINE_INTERFACES = "machine interfaces"
    MACHINE_DRIVES = "machine drives"
    MACHINE_SNAPSHOTS = "machine snapshots"
    MACHINE_ROUTING = "machine routing"
    NETWORKS = "networks"
    SHARING = "sharing"

API_URLS = {
    APICategory.AUTHENTICATION: {
        "token": {
            "url": {
                ("1.0.0", CURRENT_API_VER): "accounts/login/token/",
            },
            "methods": ["GET", "POST", "HEAD", "OPTIONS"]
        }
    },
    APICategory.USERS: {
        "list": {
            "url": {
                ("1.0.0", CURRENT_API_VER): "accounts/users/",
            },
            "methods": ["GET", "POST", "HEAD", "OPTIONS"]
        },
        "detail": {
            "url": {
                ("1.0.0", CURRENT_API_VER): "accounts/users/{pk}/",
            },
            "methods": ["GET", "PUT", "DELETE", "HEAD", "OPTIONS"]
        },
        "sharing_networks": {
            "url": {
                ("2.0.0", CURRENT_API_VER): "accounts/users/{pk}/networks/",
            },
            "methods": ["GET", "HEAD", "OPTIONS"],
        },
        "sharing_sdis": {
            "url": {
                ("2.0.0", CURRENT_API_VER): "accounts/users/{pk}/sdis/",
            },
            "methods": ["GET", "HEAD", "OPTIONS"],
        },
        "sharing_disks": {
            "url": {
                ("2.0.0", CURRENT_API_VER): "accounts/users/{pk}/disks/",
            },
            "methods": ["GET", "HEAD", "OPTIONS"],
        },
    },
    APICategory.GROUPS: {
        "list": {
            "url": {
                ("1.0.0", CURRENT_API_VER): "accounts/groups/",
            },
            "methods": ["GET", "POST", "HEAD", "OPTIONS"]
        },
        "detail": {
            "url": {
                ("1.0.0", CURRENT_API_VER): "accounts/groups/{group_pk}/",
            },
            "methods": ["GET", "PUT", "DELETE", "HEAD", "OPTIONS"]
        },
        "membership": {
            "url": {
                ("1.0.0", CURRENT_API_VER): "accounts/groups/{group_pk}/membership/",
            },
            "methods": ["GET", "PUT", "HEAD", "OPTIONS"]
        },
        "sharing_networks": {
            "url": {
                ("2.0.0", CURRENT_API_VER): "accounts/groups/{group_pk}/networks/",
            },
            "methods": ["GET", "HEAD", "OPTIONS"],
        },
        "sharing_sdis": {
            "url": {
                ("2.0.0", CURRENT_API_VER): "accounts/groups/{group_pk}/sdis/",
            },
            "methods": ["GET", "HEAD", "OPTIONS"],
        },
        "sharing_disks": {
            "url": {
                ("2.0.0", CURRENT_API_VER): "accounts/groups/{group_pk}/disks/",
            },
            "methods": ["GET", "HEAD", "OPTIONS"],
        },
    },
    APICategory.TENANCIES: {
        "list": {
            "url": {
                ("1.0.0", CURRENT_API_VER): "accounts/tenancies/",
            },
            "methods": ["GET", "POST", "HEAD", "OPTIONS"]
        },
        "detail": {
            "url": {
                ("1.0.0", CURRENT_API_VER): "accounts/tenancies/{ten_pk}/",
            },
            "methods": ["GET", "PUT", "DELETE", "HEAD", "OPTIONS"]
        },
        "security": {
            "url": {
                ("1.0.0", CURRENT_API_VER): "accounts/tenancies/{ten_pk}/security/",
            },
            "methods": ["GET", "PUT", "HEAD", "OPTIONS"]
        },
        "default": {
            "url": {
                ("1.0.0", CURRENT_API_VER): "accounts/tenancies/default/",
            },
            "methods": ["GET", "HEAD", "OPTIONS"]
        }
    },
    APICategory.SYSTEM_SETTINGS: {
        "detail": {
            "url": {
                ("1.0.0", CURRENT_API_VER): "system/settings/",
            },
            "methods": ["GET", "PUT", "HEAD", "OPTIONS"]
        },
        "physical_networks": {
            "url": {
                ("1.0.0", CURRENT_API_VER): "system/settings/physical_networks/",
            },
            "methods": ["GET", "PUT", "HEAD", "OPTIONS"]
        },
        "license": {
            "url": {
                ("1.0.0", CURRENT_API_VER): "system/settings/license/",
            },
            "methods": ["GET", "HEAD", "OPTIONS"]
        },
        "ssl": {
            "url": {
                ("1.0.0", CURRENT_API_VER): "system/settings/ssl/",
            },
            "methods": ["GET", "PUT", "HEAD", "OPTIONS"]
        },
        "version": {
            "url": {
                ("1.0.0", CURRENT_API_VER): "system/settings/version/",
            },
            "methods": ["GET", "HEAD", "OPTIONS"]
        }
    },
    APICategory.SYSTEM_STATUS: {
        "detail": {
            "url": {
                ("1.0.0", CURRENT_API_VER): "system/status/",
            },
            "methods": ["GET", "HEAD", "OPTIONS"]
        },
        "nodes": {
            "url": {
                ("1.0.0", CURRENT_API_VER): "system/status/nodes/",
            },
            "methods": ["GET", "HEAD", "OPTIONS"]
        }
    },
    APICategory.SYSTEM_TASKS: {
        "system_list": {
            "url": {
                ("1.0.0", CURRENT_API_VER): "system/tasks/",
            },
            "methods": ["GET", "HEAD", "OPTIONS"]
        },
        "user_list": {
            "url": {
                ("1.0.0", CURRENT_API_VER): "system/tasks/{pk}/",
            },
            "methods": ["GET", "HEAD", "OPTIONS"]
        },
        "user_detail": {
            "url": {
                ("1.0.0",): "system/tasks/{pk}/{lrpid}/",
                ("2.0.0", CURRENT_API_VER): "system/tasks/{lrpid}/",
            },
            "methods": ["GET", "DELETE", "HEAD", "OPTIONS"]
        },
        "reorder": {
            "url": {
                ("1.0.0", CURRENT_API_VER): "system/tasks/reorder/",
            },
            "methods": ["POST", "OPTIONS"]
        }
    },
    APICategory.DISKS: {
        "list": {
            "url": {
                ("1.0.0", CURRENT_API_VER): "storage/disks/",
            },
            "methods": ["GET", "POST", "HEAD", "OPTIONS"]
        },
        "upload_list": {
            "url": {
                ("1.0.0",): "storage/disks/{pk}/upload/",
                ("2.0.0", CURRENT_API_VER): "storage/disks/{pk}/uploads/",
            },
            "methods": ["GET", "PUT", "HEAD", "OPTIONS"]
        },
        "upload_detail": {
            "url": {
                ("1.0.0",): "storage/disks/{pk}/upload/{disk_upload_key}/",
                ("2.0.0", CURRENT_API_VER): "storage/disks/uploads/{disk_upload_key}/",
            },
            "methods": ["GET", "PUT", "DELETE", "HEAD", "OPTIONS"]
        },
        "user_list": {
            "url": {
                ("1.0.0", CURRENT_API_VER): "storage/disks/{pk}/",
            },
            "methods": ["GET", "POST", "HEAD", "OPTIONS"]
        },
        "user_detail": {
            "url": {
                ("1.0.0",): "storage/disks/{pk}/{image_id}/",
                ("2.0.0", CURRENT_API_VER): "storage/disks/{image_id}/",
            },
            "methods": ["GET", "PUT", "DELETE", "HEAD", "OPTIONS"]
        },
        "copy": {
            "url": {
                ("1.0.0",): "storage/disks/{pk}/{image_id}/copy/",
                ("2.0.0", CURRENT_API_VER): "storage/disks/{image_id}/copy/",
            },
            "methods": ["POST", "HEAD", "OPTIONS"]
        },
        "permissions": {
            "url": {
                ("1.0.0",): "storage/disks/{pk}/{image_id}/permissions/",
                ("2.0.0", CURRENT_API_VER): "storage/disks/{image_id}/permissions/",
            },
            "methods": ["GET", "PUT", "HEAD", "OPTIONS"]
        }
    },
    APICategory.GENERAL: {
        "list": {
            "url": {
                ("1.0.0", CURRENT_API_VER): "storage/general/",
            },
            "methods": ["GET", "HEAD", "OPTIONS"]
        },
        "user_list": {
            "url": {
                ("1.0.0", CURRENT_API_VER): "storage/general/{pk}/",
            },
            "methods": ["GET", "POST", "HEAD", "OPTIONS"]
        },
        "directory_list": {
            "url": {
                ("1.0.0", CURRENT_API_VER): "storage/general/{pk}/directory/{directory_key}/",
            },
            "methods": ["GET", "POST", "DELETE", "HEAD", "OPTIONS"]
        },
        "file_details": {
            "url": {
                ("1.0.0", CURRENT_API_VER): "storage/general/{pk}/file/{file_key}/",
            },
            "methods": ["GET", "DELETE", "HEAD", "OPTIONS"]
        },
        "file_move": {
            "url": {
                ("1.0.0", CURRENT_API_VER): "storage/general/{pk}/file/{file_key}/move/",
            },
            "methods": ["PUT", "HEAD", "OPTIONS"]
        },
        "upload_list": {
            "url": {
                ("1.0.0",): "storage/general/{pk}/upload/",
                ("2.0.0", CURRENT_API_VER): "storage/general/{pk}/uploads/",
            },
            "methods": ["GET", "POST", "HEAD", "OPTIONS"]
        },
        "upload_details": {
            "url": {
                ("1.0.0",): "storage/general/{pk}/upload/{general_upload_key}/",
                ("2.0.0", CURRENT_API_VER): "storage/general/uploads/{general_upload_key}/",
            },
            "methods": ["GET", "PUT", "DELETE", "HEAD", "OPTIONS"]
        }
    },
    APICategory.SDI_FILES: {
        "list": {
            "url": {
                ("1.0.0",): "storage/ici/",
                ("2.0.0", CURRENT_API_VER): "storage/sdi/",
            },
            "methods": ["GET", "HEAD", "OPTIONS"]
        },
        "user_list": {
            "url": {
                ("1.0.0",): "storage/ici/{pk}/",
                ("2.0.0", CURRENT_API_VER): "storage/sdi/{pk}/",
            },
            "methods": ["GET", "HEAD", "OPTIONS"]
        },
        "file_detail": {
            "url": {
                ("1.0.0",): "storage/ici/{pk}/file/{file_key}/",
                ("2.0.0", CURRENT_API_VER): "storage/sdi/{pk}/file/{file_key}/",
            },
            "methods": ["GET", "DELETE", "HEAD", "OPTIONS"]
        },
        "import": {
            "url": {
                ("1.0.0",): "storage/ici/{pk}/file/{file_key}/import/",
                ("2.0.0", CURRENT_API_VER): "storage/sdi/{pk}/file/{file_key}/import/",
            },
            "methods": ["PUT", "HEAD", "OPTIONS"]
        },
        "upload_list": {
            "url": {
                ("1.0.0",): "storage/ici/{pk}/upload/",
                ("2.0.0", CURRENT_API_VER): "storage/sdi/{pk}/uploads/",
            },
            "methods": ["GET", "POST", "HEAD", "OPTIONS"]
        },
        "upload_detail": {
            "url": {
                ("1.0.0",): "storage/ici/{pk}/upload/{file_upload_key}/",
                ("2.0.0", CURRENT_API_VER): "storage/sdi/uploads/{file_upload_key}/",
            },
            "methods": ["GET", "PUT", "DELETE", "HEAD", "OPTIONS"]
        }
    },
    APICategory.SDIS: {
        "list": {
            "url": {
                ("1.0.0",): "clouds/",
                ("2.0.0", CURRENT_API_VER): "sdis/",
            },
            "methods": ["GET", "HEAD", "OPTIONS"]
        },
        "user_list": {
            "url": {
                ("1.0.0",): "clouds/{pk}/",
                ("2.0.0", CURRENT_API_VER): "sdis/{pk}/",
            },
            "methods": ["GET", "POST", "HEAD", "OPTIONS"]
        },
        "user_detail": {
            "url": {
                ("1.0.0",): "clouds/{pk}/{sdi_id}/",
                ("2.0.0", CURRENT_API_VER): "sdis/{sdi_id}/",
            },
            "methods": ["GET", "PUT", "DELETE", "HEAD", "OPTIONS"]
        },
        "copy": {
            "url": {
                ("1.0.0",): "clouds/{pk}/{sdi_id}/copy/",
                ("2.0.0", CURRENT_API_VER): "sdis/{sdi_id}/copy/",
            },
            "methods": ["POST", "HEAD", "OPTIONS"]
        },
        "export": {
            "url": {
                ("1.0.0",): "clouds/{pk}/{sdi_id}/export/",
                ("2.0.0", CURRENT_API_VER): "sdis/{sdi_id}/export/",
            },
            "methods": ["POST", "HEAD", "OPTIONS"]
        },
        "permissions": {
            "url": {
                ("1.0.0",): "clouds/{pk}/{sdi_id}/permissions/",
                ("2.0.0", CURRENT_API_VER): "sdis/{sdi_id}/permissions/",
            },
            "methods": ["GET", "PUT", "HEAD", "OPTIONS"]
        },
        "start": {
            "url": {
                ("1.0.0",): "clouds/{pk}/{sdi_id}/start/",
                ("2.0.0", CURRENT_API_VER): "sdis/{sdi_id}/start/",
            },
            "methods": ["POST", "HEAD", "OPTIONS"]
        },
        "stop": {
            "url": {
                ("1.0.0",): "clouds/{pk}/{sdi_id}/stop/",
                ("2.0.0", CURRENT_API_VER): "sdis/{sdi_id}/stop/",
            },
            "methods": ["POST", "HEAD", "OPTIONS"]
        },
        "settings": {
            "url": {
                ("1.0.0",): "clouds/{pk}/{sdi_id}/settings/",
                ("2.0.0", CURRENT_API_VER): "sdis/{sdi_id}/settings/",
            },
            "methods": ["GET", "PUT", "HEAD", "OPTIONS"]
        },
        "checkpoint": {
            "url": {
                ("1.0.0",): "clouds/{pk}/{sdi_id}/checkpoints/",
                ("2.0.0", CURRENT_API_VER): "sdis/{sdi_id}/checkpoints/",
            },
            "methods": ["GET", "POST", "HEAD", "OPTIONS"]
        },
        "checkpoint_detail": {
            "url": {
                ("1.0.0",): "clouds/{pk}/{sdi_id}/checkpoints/{check_tag}/",
                ("2.0.0", CURRENT_API_VER): "sdis/{sdi_id}/checkpoints/{check_tag}/",
            },
            "methods": ["GET", "PUT", "DELETE", "HEAD", "OPTIONS"]
        },
        "port_list": {
            "url": {
                ("1.0.0",): "clouds/{pk}/{sdi_id}/ports/",
                ("2.0.0", CURRENT_API_VER): "sdis/{sdi_id}/ports/",
            },
            "methods": ["GET", "POST", "HEAD", "OPTIONS"]
        },
        "history": {
            "url": {
                ("1.0.0",): "clouds/{pk}/{sdi_id}/history/",
                ("2.0.0", CURRENT_API_VER): "sdis/{sdi_id}/history/",
            },
            "methods": ["GET", "HEAD", "OPTIONS"]
        },
        "status": {
            "url": {
                ("1.0.0",): "clouds/{pk}/{sdi_id}/status/",
                ("2.0.0", CURRENT_API_VER): "sdis/{sdi_id}/status/",
            },
            "methods": ["GET", "HEAD", "OPTIONS"]
        },
        "persist": {
            "url": {
                ("1.0.0",): "clouds/{pk}/{sdi_id}/persist/",
                ("2.0.0", CURRENT_API_VER): "sdis/{sdi_id}/persist/",
            },
            "methods": ["GET", "PUT", "HEAD", "OPTIONS"]
        },
        "overview": {
            "url": {
                ("1.0.0",): "clouds/{pk}/{sdi_id}/overview/",
                ("2.0.0", CURRENT_API_VER): "sdis/{sdi_id}/overview/",
            },
            "methods": ["GET", "HEAD", "OPTIONS"]
        }
    },
    APICategory.MACHINES: {
        "list": {
            "url": {
                ("1.0.0",): "clouds/{pk}/{sdi_id}/machines/",
                ("2.0.0", CURRENT_API_VER): "sdis/{sdi_id}/machines/",
            },
            "methods": ["GET", "POST", "HEAD", "OPTIONS"]
        },
        "detail": {
            "url": {
                ("1.0.0",): "clouds/{pk}/{sdi_id}/machines/{machine_id}/",
                ("2.0.0", CURRENT_API_VER): "sdis/{sdi_id}/machines/{machine_id}/",
            },
            "methods": ["GET", "PUT", "DELETE", "HEAD", "OPTIONS"]
        },
        "vnc": {
            "url": {
                ("1.0.0",): "clouds/{pk}/{sdi_id}/machines/{machine_id}/vnc/",
                ("2.0.0", CURRENT_API_VER): "sdis/{sdi_id}/machines/{machine_id}/vnc/",
            },
            "methods": ["GET", "HEAD", "OPTIONS"]
        },
        "status": {
            "url": {
                ("1.0.0",): "clouds/{pk}/{sdi_id}/machines/{machine_id}/status/",
                ("2.0.0", CURRENT_API_VER): "sdis/{sdi_id}/machines/{machine_id}/status/",
            },
            "methods": ["GET", "HEAD", "OPTIONS"]
        },
        "start": {
            "url": {
                ("1.0.0",): "clouds/{pk}/{sdi_id}/machines/{machine_id}/start/",
                ("2.0.0", CURRENT_API_VER): "sdis/{sdi_id}/machines/{machine_id}/start/",
            },
            "methods": ["PUT", "OPTIONS"]
        },
        "stop": {
            "url": {
                ("1.0.0",): "clouds/{pk}/{sdi_id}/machines/{machine_id}/stop/",
                ("2.0.0", CURRENT_API_VER): "sdis/{sdi_id}/machines/{machine_id}/stop/",
            },
            "methods": ["PUT", "OPTIONS"]
        },
        "power_off": {
            "url": {
                ("1.0.0",): "clouds/{pk}/{sdi_id}/machines/{machine_id}/power_off/",
                ("2.0.0", CURRENT_API_VER): "sdis/{sdi_id}/machines/{machine_id}/power_off/",
            },
            "methods": ["PUT", "OPTIONS"]
        },
        "resume": {
            "url": {
                ("1.0.0",): "clouds/{pk}/{sdi_id}/machines/{machine_id}/resume/",
                ("2.0.0", CURRENT_API_VER): "sdis/{sdi_id}/machines/{machine_id}/resume/",
            },
            "methods": ["PUT", "OPTIONS"]
        },
        "suspend": {
            "url": {
                ("1.0.0",): "clouds/{pk}/{sdi_id}/machines/{machine_id}/suspend/",
                ("2.0.0", CURRENT_API_VER): "sdis/{sdi_id}/machines/{machine_id}/suspend/",
            },
            "methods": ["PUT", "OPTIONS"]
        },
    },
    APICategory.MACHINE_INTERFACES: {
        "list": {
            "url": {
                ("1.0.0",): "clouds/{pk}/{sdi_id}/machines/{machine_id}/interfaces/",
                ("2.0.0", CURRENT_API_VER): "sdis/{sdi_id}/machines/{machine_id}/interfaces/",
            },
            "methods": ["GET", "POST", "HEAD", "OPTIONS"]
        },
        "detail": {
            "url": {
                ("1.0.0",): "clouds/{pk}/{sdi_id}/machines/{machine_id}/interfaces/{connection_id}/",
                ("2.0.0", CURRENT_API_VER): "sdis/{sdi_id}/machines/{machine_id}/interfaces/{connection_id}/",
            },
            "methods": ["GET", "PUT", "DELETE", "HEAD", "OPTIONS"]
        },
        "port_list": {
            "url": {
                ("1.0.0",): "clouds/{pk}/{sdi_id}/machines/{machine_id}/interfaces/{connection_id}/ports/",
                ("2.0.0", CURRENT_API_VER): "sdis/{sdi_id}/machines/{machine_id}/interfaces/{connection_id}/ports/",
            },
            "methods": ["GET", "HEAD", "OPTIONS"],
        },
        "vlan_list": {
            "url": {
                ("1.0.0",): "clouds/{pk}/{sdi_id}/machines/{machine_id}/interfaces/{connection_id}/vlans/",
                ("2.0.0", CURRENT_API_VER): "sdis/{sdi_id}/machines/{machine_id}/interfaces/{connection_id}/vlans/",
            },
            "methods": ["GET", "POST", "HEAD", "OPTIONS"],
        },
        "vlan_detail": {
            "url": {
                ("1.0.0",): "clouds/{pk}/{sdi_id}/machines/{machine_id}/interfaces/{connection_id}/vlans/{vlan_id}/",
                ("2.0.0", CURRENT_API_VER): "sdis/{sdi_id}/machines/{machine_id}/interfaces/{connection_id}/vlans/{vlan_id}/",
            },
            "methods": ["GET", "PUT", "DELETE", "HEAD", "OPTIONS"],
        },
        "vlan_port_list": {
            "url": {
                ("1.0.0",): "clouds/{pk}/{sdi_id}/machines/{machine_id}/interfaces/{connection_id}/vlans/{vlan_id}/ports/",
                ("2.0.0", CURRENT_API_VER): "sdis/{sdi_id}/machines/{machine_id}/interfaces/{connection_id}/vlans/{vlan_id}/ports/",
            },
            "methods": ["GET", "POST", "HEAD", "OPTIONS"],
        },
        "vlan_port_detail": {
            "url": {
                ("1.0.0",): "clouds/{pk}/{sdi_id}/machines/{machine_id}/interfaces/{connection_id}/vlans/{vlan_id}/ports/{port_id}",
                ("2.0.0", CURRENT_API_VER): "sdis/{sdi_id}/machines/{machine_id}/interfaces/{connection_id}/vlans/{vlan_id}/ports/{port_id}",
            },
            "methods": ["GET", "DELETE", "HEAD", "OPTIONS"],
        },
    },
    APICategory.MACHINE_DRIVES: {
        "list": {
            "url": {
                ("1.0.0",): "clouds/{pk}/{sdi_id}/machines/{machine_id}/drives/",
                ("2.0.0", CURRENT_API_VER): "sdis/{sdi_id}/machines/{machine_id}/drives/",
            },
            "methods": ["GET", "POST", "HEAD", "OPTIONS"]
        },
        "order": {
            "url": {
                ("1.0.0",): "clouds/{pk}/{sdi_id}/machines/{machine_id}/drives/order/",
                ("2.0.0", CURRENT_API_VER): "sdis/{sdi_id}/machines/{machine_id}/drives/order/",
            },
            "methods": ["GET", "PUT", "HEAD", "OPTIONS"]
        },
        "detail": {
            "url": {
                ("1.0.0",): "clouds/{pk}/{sdi_id}/machines/{machine_id}/drives/{disk_slot}/",
                ("2.0.0", CURRENT_API_VER): "sdis/{sdi_id}/machines/{machine_id}/drives/{disk_slot}/",
            },
            "methods": ["GET", "PUT", "DELETE", "HEAD", "OPTIONS"]
        },
        "save_new": {
            "url": {
                ("1.0.0",): "clouds/{pk}/{sdi_id}/machines/{machine_id}/drives/{disk_slot}/save_new/",
                ("2.0.0", CURRENT_API_VER): "sdis/{sdi_id}/machines/{machine_id}/drives/{disk_slot}/save_new/",
            },
            "methods": ["PUT", "HEAD", "OPTIONS"]
        },
        "save_base": {
            "url": {
                ("1.0.0",): "clouds/{pk}/{sdi_id}/machines/{machine_id}/drives/{disk_slot}/save_base/",
                ("2.0.0", CURRENT_API_VER): "sdis/{sdi_id}/machines/{machine_id}/drives/{disk_slot}/save_base/",
            },
            "methods": ["PUT", "HEAD", "OPTIONS"]
        }
    },
    APICategory.MACHINE_SNAPSHOTS: {
        "list": {
            "url": {
                ("1.0.0",): "clouds/{pk}/{sdi_id}/machines/{machine_id}/snapshots/",
                ("2.0.0", CURRENT_API_VER): "sdis/{sdi_id}/machines/{machine_id}/snapshots/",
            },
            "methods": ["GET", "POST", "HEAD", "OPTIONS"]
        },
        "detail": {
            "url": {
                ("1.0.0",): "clouds/{pk}/{sdi_id}/machines/{machine_id}/snapshots/{snap_tag}/",
                ("2.0.0", CURRENT_API_VER): "sdis/{sdi_id}/machines/{machine_id}/snapshots/{snap_tag}/",
            },
            "methods": ["GET", "PUT", "DELETE", "HEAD", "OPTIONS"]
        }
    },
    APICategory.MACHINE_ROUTING: {
        "detail": {
            "url": {
                ("1.0.0",): "clouds/{pk}/{sdi_id}/machines/{machine_id}/routing/",
                ("2.0.0", CURRENT_API_VER): "sdis/{sdi_id}/machines/{machine_id}/routing/",
            },
            "methods": ["GET", "HEAD", "OPTIONS"]
        },
        "settings": {
            "url": {
                ("1.0.0",): "clouds/{pk}/{sdi_id}/machines/{machine_id}/routing/settings/",
                ("2.0.0", CURRENT_API_VER): "sdis/{sdi_id}/machines/{machine_id}/routing/settings/",
            },
            "methods": ["GET", "PUT", "HEAD", "OPTIONS"]
        },
        "keychains": {
            "url": {
                ("1.0.0",): "clouds/{pk}/{sdi_id}/machines/{machine_id}/routing/keychains/",
                ("2.0.0", CURRENT_API_VER): "sdis/{sdi_id}/machines/{machine_id}/routing/keychains/",
            },
            "methods": ["GET", "PUT", "HEAD", "OPTIONS"]
        },
        "interface_list": {
            "url": {
                ("1.0.0",): "clouds/{pk}/{sdi_id}/machines/{machine_id}/routing/interfaces/",
                ("2.0.0", CURRENT_API_VER): "sdis/{sdi_id}/machines/{machine_id}/routing/interfaces/",
            },
            "methods": ["GET", "HEAD", "OPTIONS"]
        },
        "interface_detail": {
            "url": {
                ("1.0.0",): "clouds/{pk}/{sdi_id}/machines/{machine_id}/routing/interfaces/{connection_id}/",
                ("2.0.0", CURRENT_API_VER): "sdis/{sdi_id}/machines/{machine_id}/routing/interfaces/{connection_id}/",
            },
            "methods": ["GET", "PUT", "HEAD", "OPTIONS"]
        }
    },
    APICategory.NETWORKS: {
        "list": {
            "url": {
                ("1.0.0",): "clouds/{pk}/{sdi_id}/networks/",
                ("2.0.0", CURRENT_API_VER): "sdis/{sdi_id}/networks/",
            },
            "methods": ["GET", "POST", "HEAD", "OPTIONS"]
        },
        "detail": {
            "url": {
                ("1.0.0",): "clouds/{pk}/{sdi_id}/networks/{network_id}/",
                ("2.0.0", CURRENT_API_VER): "sdis/{sdi_id}/networks/{network_id}/",
            },
            "methods": ["GET", "PUT", "DELETE", "HEAD", "OPTIONS"]
        },
        "replug": {
            "url": {
                ("1.0.0",): "clouds/{pk}/{sdi_id}/networks/{network_id}/replug/",
                ("2.0.0", CURRENT_API_VER): "sdis/{sdi_id}/networks/{network_id}/replug/",
            },
            "methods": ["PUT", "HEAD", "OPTIONS"]
        },
        "service_list": {
            "url": {
                ("1.0.0",): "clouds/{pk}/{sdi_id}/networks/{network_id}/services/",
                ("2.0.0", CURRENT_API_VER): "sdis/{sdi_id}/networks/{network_id}/services/",
            },
            "methods": ["GET", "POST", "HEAD", "OPTIONS"],
        },
        "service_detail": {
            "url": {
                ("1.0.0",): "clouds/{pk}/{sdi_id}/networks/{network_id}/services/{service_id}/",
                ("2.0.0", CURRENT_API_VER): "sdis/{sdi_id}/networks/{network_id}/services/{service_id}/",
            },
            "methods": ["GET", "PUT", "DELETE", "HEAD", "OPTIONS"],
        },
        "pool_list": {
            "url": {
                ("1.0.0",): "clouds/{pk}/{sdi_id}/networks/{network_id}/services/{service_id}/pools/",
                ("2.0.0", CURRENT_API_VER): "sdis/{sdi_id}/networks/{network_id}/services/{service_id}/pools/",
            },
            "methods": ["GET", "POST", "HEAD", "OPTIONS"]
        },
        "pool_detail": {
            "url": {
                ("1.0.0",): "clouds/{pk}/{sdi_id}/networks/{network_id}/services/{service_id}/pools/{pool_id}/",
                ("2.0.0", CURRENT_API_VER): "sdis/{sdi_id}/networks/{network_id}/services/{service_id}/pools/{pool_id}/",
            },
            "methods": ["GET", "PUT", "DELETE", "HEAD", "OPTIONS"]
        }
    },
    APICategory.SHARING: {
        "network_list": {
            "url": {
                ("1.0.0",): "sharing/networks/",
            },
            "methods": ["GET", "HEAD", "OPTIONS"]
        },
        "user_list": {
            "url": {
                ("1.0.0",): "sharing/networks/users/",
            },
            "methods": ["GET", "HEAD", "OPTIONS"]
        },
        "user_detail": {
            "url": {
                ("1.0.0",): "sharing/networks/users/{pk}/",
                ("2.0.0", CURRENT_API_VER): "accounts/users/{pk}/networks/",
            },
            "methods": ["GET", "HEAD", "OPTIONS"]
        },
        "group_list": {
            "url": {
                ("1.0.0",): "sharing/networks/groups/",
            },
            "methods": ["GET", "HEAD", "OPTIONS"]
        },
        "group_detail": {
            "url": {
                ("1.0.0",): "sharing/networks/groups/{group_pk}/",
                ("2.0.0", CURRENT_API_VER): "accounts/groups/{group_pk}/networks/",
            },
            "methods": ["GET", "HEAD", "OPTIONS"]
        }
    }
}    #type: Dict[APICategory, Dict[str, Any]]


OAUTH_TOOLKIT = {
    "token": "o/token/",
    "register": "o/applications/register/",
    "update": "o/applications/{}/update/"
}
