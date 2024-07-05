from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import insert, select
from sqlalchemy.orm import Session
from typing import Annotated

from database import get_async_session

from .models import Image, UserOrder
from .schemas import ImageCreate, UserOrderCreate

router = APIRouter(prefix="/servers")
    
@router.post("", status_code=201)
async def create_server(post: UserOrderCreate, session: Annotated[Session, Depends(get_async_session)]):
    quiery = insert(UserOrder).values(**post.model_dump())
    await session.execute(quiery)
    await session.commit()
    return {"status": "success"}

@router.get("/images")
async def get_image_templates(session: Annotated[Session, Depends(get_async_session)]):
    quiery = select(Image)
    try:
        result = await session.execute(quiery)
        return {
                "status": "success",
                "data": result.scalars().all(),
                "details": None
            }
    except Exception:
        raise HTTPException(status_code=500, detail={
            "status": "error",
            "data": None,
            "details": None
        })

@router.get("/my-images")
async def get_my_images(session: Annotated[Session, Depends(get_async_session)]):
    quiery = select(Image)
    try:
        result = await session.execute(quiery)
        return {
                "status": "success",
                "data": result.scalars().all(),
                "details": None
            }
    except Exception:
        raise HTTPException(status_code=500, detail={
            "status": "error",
            "data": None,
            "details": None
        })

@router.post("/my-images/create", status_code=201)
async def create_image(image: ImageCreate, session: Annotated[Session, Depends(get_async_session)]):
    quiery = insert(Image).values(**image.model_dump())
    await session.execute(quiery)
    await session.commit()
    return {"status": "success"}