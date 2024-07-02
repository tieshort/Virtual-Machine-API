from sqlalchemy.orm import Session
from database.dataBase import User, Image, UserOrder
from database.pyDantic import UserCreate, ImageCreate, UserOrderCreate
import hashlib

def create_user(db_session: Session, user_data: dict):
    user = UserCreate(**user_data)
    hashed_password = hash_password(user.password)
    db_user = User(name=user.name, password=hashed_password, email=user.email, phone=user.phone)
    db_session.add(db_user)
    db_session.commit()
    db_session.refresh(db_user)
    return db_user

def create_image(db_session: Session, image_data: dict):
    image = ImageCreate(**image_data)
    db_image = Image(name=image.name, operating_system=image.operating_system,
                     memory=image.memory, disk=image.disk)
    db_session.add(db_image)
    db_session.commit()
    db_session.refresh(db_image)
    return db_image

def create_user_order(db_session: Session, user_order_data: dict):
    user_order = UserOrderCreate(**user_order_data)
    db_user_order = UserOrder(name=user_order.name, configuration=user_order.configuration,
                              network=user_order.network, access=user_order.access,
                              cloud_ini=user_order.cloud_ini, image_id=user_order.image_id,
                              user_id=user_order.user_id)
    db_session.add(db_user_order)
    db_session.commit()
    db_session.refresh(db_user_order)
    return db_user_order

def hash_password(plaintext_password: str) -> str:
    return hashlib.sha256(plaintext_password.encode()).hexdigest()

def get_user_info(db_session: Session, user_id: int):
    user = db_session.query(User).filter(User.id == user_id).first()
    if not user:
        return None

    user_orders = db_session.query(UserOrder).filter(UserOrder.user_id == user_id).all()
    orders_with_images = []
    for order in user_orders:
        image = db_session.query(Image).filter(Image.id == order.image_id).first()
        orders_with_images.append({
            "order": order,
            "image": image
        })

    return {
        "user": user,
        "orders_with_images": orders_with_images
    }
