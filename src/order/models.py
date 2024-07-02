from sqlalchemy import JSON, Column, ForeignKey, Integer, String
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, unique=True, index=True)
    name = Column(String, index=True, nullable=False)
    password = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    phone = Column(String, nullable=False)

    orders = relationship("UserOrder", back_populates="user")

class Image(Base):
    __tablename__ = 'images'

    id = Column(Integer, primary_key=True, unique=True, index=True)
    name = Column(String, index=True, nullable=False)
    operating_system = Column(String, nullable=False)
    memory = Column(Integer, nullable=False)
    disk = Column(Integer, nullable=False)

    orders = relationship("UserOrder", back_populates="image")

class UserOrder(Base):
    __tablename__ = 'user_orders'

    id = Column(Integer, primary_key=True, unique=True, index=True)
    name = Column(String, nullable=False)
    configuration = Column(JSON, nullable=False)
    network = Column(JSON, nullable=False)
    access = Column(JSON, nullable=False)
    cloud_ini = Column(JSON, nullable=False)

    image_id = Column(Integer, ForeignKey('images.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    user = relationship("User", back_populates="orders")
    image = relationship("Image", back_populates="orders")