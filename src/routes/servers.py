from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/servers")

class Server(BaseModel):
    id: int
    name: str
    memory: str
    

@router.post("")
async def create_server(server: Server):
    return server

@router.get("/images")
async def get_image_templates():
    pass

@router.get("/myImages")
async def get_my_images():
    pass