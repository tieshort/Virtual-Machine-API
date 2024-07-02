from sqlalchemy import Column, Integer, String, JSON, ForeignKey, create_engine
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id: int = Column(Integer, primary_key=True, unique=True, index=True)
    name: str = Column(String, index=True, nullable=False)
    password: str = Column(String, nullable=False)
    email: str = Column(String, unique=True, index=True, nullable=False)
    phone: str = Column(String, nullable=False)

    orders = relationship("UserOrder", back_populates="user")

class Image(Base):
    __tablename__ = 'images'

    id: int = Column(Integer, primary_key=True, unique=True, index=True)
    name: str = Column(String, index=True, nullable=False)
    operating_system: str = Column(String, nullable=False)
    memory: int = Column(Integer, nullable=False)
    disk: int = Column(Integer, nullable=False)

    orders = relationship("UserOrder", back_populates="image")

class UserOrder(Base):
    __tablename__ = 'user_orders'

    id: int = Column(Integer, primary_key=True, unique=True, index=True)
    name: str = Column(String, nullable=False)
    configuration: dict[str, any] = Column(JSON, nullable=False)
    network: dict[str, any] = Column(JSON, nullable=False)
    access: dict[str, any] = Column(JSON, nullable=False)
    cloud_ini: dict[str, any] = Column(JSON, nullable=False)

    image_id: int = Column(Integer, ForeignKey('images.id'), nullable=False)
    user_id: int = Column(Integer, ForeignKey('users.id'), nullable=False)

    user = relationship("User", back_populates="orders")
    image = relationship("Image", back_populates="orders")

# create database
engine = create_engine('sqlite:///example.db', echo=False)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
