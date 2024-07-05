from fastapi import APIRouter, Depends
from fastapi.middleware import Middleware
from starlette.middleware.base import BaseHTTPMiddleware

router = APIRouter(prefix="/{user_id}/vms")

@router.get("")
async def get_vms(user_id: int):
    pass

@router.get("/{vm_id}/panel/config")
async def get_panel_config(user_id: int, vm_id: str):
    pass

@router.get("/{vm_id}/panel/console")
async def get_panel_console(user_id: int, vm_id: str):
    pass

@router.post("/{vm_id}/panel/start_vm")
async def start_vm(user_id: int, vm_id: str):
    pass

@router.post("/{vm_id}/panel/stop_vm")
async def stop_vm(user_id: int, vm_id: str):
    pass

@router.post("/{vm_id}/panel/retart_vm")
async def retart_vm(user_id: int, vm_id: str):
    pass