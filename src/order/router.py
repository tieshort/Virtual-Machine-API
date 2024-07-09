from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session

from .models import Image, UserOrder  # type: ignore
from .schemas import ImageCreate, UserOrderCreate  # type: ignore

router = APIRouter(prefix="/servers")


@router.post("", status_code=status.HTTP_201_CREATED)
async def create_server(
    post: UserOrderCreate, 
    session: Annotated[AsyncSession, Depends(get_async_session)]
    ):
    query = insert(UserOrder).values(**post.model_dump())
    await session.execute(query)
    await session.commit()
    return {
        "status": "success"
        }


@router.get("/images", status_code=status.HTTP_200_OK)
async def get_image_templates(
    session: Annotated[AsyncSession, Depends(get_async_session)]
    ):
    query = select(Image)
    try:
        result = await session.execute(query)
        return {
            "status": "success", 
            "data": result.scalars().all(), 
            "details": None
            }
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail={
                "status": "error", 
                "data": None, 
                "details": None
                }
        )


@router.get("/my-images", status_code=status.HTTP_200_OK)
async def get_my_images(
    session: Annotated[AsyncSession, Depends(get_async_session)]
    ):
    quiery = select(Image)
    try:
        result = await session.execute(quiery)
        return {
            "status": "success", 
            "data": result.scalars().all(), 
            "details": None
            }
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail={
                "status": "error", 
                "data": None, 
                "details": None}
        )


@router.post("/my-images/create", status_code=status.HTTP_201_CREATED)
async def create_image(
    image: ImageCreate, 
    session: Annotated[AsyncSession, Depends(get_async_session)]
    ):
    quiery = insert(Image).values(**image.model_dump())
    await session.execute(quiery)
    await session.commit()
    return {
        "status": "success"
        }