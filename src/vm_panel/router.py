from fastapi import APIRouter, Depends, status

from middleware.auth_middleware import check_auth_header

router = APIRouter()

vm_data = {
    "1": {"name": "test", "status": "active", "ip": "10.0.2.214"},
    "2": {"name": "test2", "status": "active", "ip": "10.0.2.215"},
}

vm_config_data = {
    "1": {"config": {"os": "debian-11", "hdd": 40, "ram": 2, "status": "active"}},
    "2": {"config": {"os": "ubuntu-20.04", "hdd": 50, "ram": 4, "status": "inactive"}},
}


vm_console_data = {
    "1": {"url": "<div>some body html for vm1</div>"},
    "2": {"url": "<div>some body html for vm2</div>"},
}


@router.get("/{user_id}/vms", 
        dependencies=[Depends(check_auth_header)], 
        status_code=status.HTTP_200_OK)
async def get_vms(user_id: int):
    response = str(vm_data)
    return {
        "status": "success",
        "data": response,
    }


@router.get("/{user_id}/vms/{vm_id}/panel/config", 
        dependencies=[Depends(check_auth_header)],
        status_code=status.HTTP_200_OK)
async def get_panel_config(user_id: int, vm_id: str):
    response = f"vm_id: {vm_id}, config: {vm_config_data.get(vm_id).get('config')}"
    return {
        "status": "success",
        "data": response,
    }


@router.get("/{user_id}/vms/{vm_id}/panel/console", 
        dependencies=[Depends(check_auth_header)],
        status_code=status.HTTP_200_OK)
async def get_panel_console(user_id: int, vm_id: str):
    response = f"vm_id: {vm_id}, url: {vm_console_data.get(vm_id).get('url')}"
    return {
        "status": "success",
        "data": response,
    }


@router.post("/{user_id}/vms/{vm_id}/panel/start_vm", 
        dependencies=[Depends(check_auth_header)])
async def start_vm(user_id: int, vm_id: int):
    pass


@router.post("/{user_id}/vms/{vm_id}/panel/stop_vm", 
        dependencies=[Depends(check_auth_header)])
async def stop_vm(user_id: int, vm_id: int):
    pass


@router.post("/{user_id}/vms/{vm_id}/panel/restart_vm", 
        dependencies=[Depends(check_auth_header)])
async def retart_vm(user_id: int, vm_id: int):
    pass
