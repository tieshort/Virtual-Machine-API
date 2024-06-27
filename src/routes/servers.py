from fastapi import APIRouter

router = APIRouter(prefix="/servers")

@router.post("")
async def create_server():
    pass

@router.get("/images")
async def get_image_templates():
    pass

@router.get("/myImages")
async def get_my_images():
    pass