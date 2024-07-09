from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import insert, select
from sqlalchemy.orm import Session

from database import get_async_session

from .models import Image, UserOrder
from .schemas import ImageCreate, ImageRead, UserOrderCreate

router = APIRouter(prefix="/servers")
    
@router.post("")
async def create_server(post: UserOrderCreate, session: Session = Depends(get_async_session)):
    quiery = insert(UserOrder).values(**post.model_dump())
    await session.execute(quiery)
    await session.commit()
    return {"status": "succes"}

@router.get("/images", response_model=list[ImageRead])
async def get_image_templates(session: Session = Depends(get_async_session)):
    quiery = select(Image)
    try:
        result = await session.execute(quiery)
        return {
                "status": "success",
                "data": result.all(),
                "details": None
            }
    except Exception:
        raise HTTPException(status_code=500, detail={
            "status": "error",
            "data": None,
            "details": None
        })

@router.get("/my-images", response_model=list[ImageRead])
async def get_my_images(session: Session = Depends(get_async_session)):
    quiery = select(Image)
    try:
        result = await session.execute(quiery)
        return {
                "status": "success",
                "data": result.all(),
                "details": None
            }
    except Exception:
        raise HTTPException(status_code=500, detail={
            "status": "error",
            "data": None,
            "details": None
        })

@router.post("/my-images/create")
async def create_image(image: ImageCreate, session: Session = Depends(get_async_session)):
    quiery = insert(Image).values(**image.model_dump())
    await session.execute(quiery)
    await session.commit()
    return {"status": "succes"}