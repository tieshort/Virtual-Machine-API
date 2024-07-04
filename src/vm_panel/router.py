from fastapi import APIRouter

router = APIRouter(prefix="{user_id}/vms")

@router.get("")
async def get_vms():
    pass

@router.get("/{vm_id}/panel/config")
async def get_panel_config(vm_id: str):
    pass

@router.post("/{vm_id}/panel/start_vm")
async def start_vm(vm_id: str):
    pass

@router.post("/{vm_id}/panel/stop_vm")
async def stop_vm(vm_id: str):
    pass

@router.post("/{vm_id}/panel/retart_vm")
async def retart_vm(vm_id: str):
    pass