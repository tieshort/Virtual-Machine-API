from sqlalchemy import ForeignKey, create_engine, JSON
from sqlalchemy.orm import relationship, sessionmaker, declarative_base, Mapped, mapped_column

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column (primary_key=True, unique=True, index=True)
    name: Mapped[str] = mapped_column(index=True, nullable=False)
    password: Mapped[str] = mapped_column( nullable=False)
    email: Mapped[str] = mapped_column( unique=True, index=True, nullable=False)
    phone: Mapped[str] = mapped_column(nullable=False, unique=True)

    orders = relationship("UserOrder", back_populates="user")

class Image(Base):
    __tablename__ = 'images'

    id: Mapped[int] = mapped_column(primary_key=True, unique=True, index=True)
    name: Mapped[str] = mapped_column(index=True, nullable=False)
    operating_system: Mapped[str] = mapped_column(nullable=False)
    memory: Mapped[str] = mapped_column(nullable=False)
    disk: Mapped[str] = mapped_column(nullable=False)

    orders = relationship("UserOrder", back_populates="image")

# class CustomImage (Image):
#     __tablename__ = 'custom_images'
#     id: Mapped[int] = mapped_column(primary_key=True, unique=True, index=True)
#
#     custom_orders = relationship("UserOrder", back_populates="custom_image")

class CustomImage(Base):
    __tablename__ = 'custom_images'

    id: Mapped[int] = mapped_column(primary_key=True, unique=True, index=True)
    name: Mapped[str] = mapped_column(index=True, nullable=False)
    load_file:  Mapped[str] = mapped_column( nullable=False)
    user_id:  Mapped[int] = mapped_column(nullable=False)
    operating_system: Mapped[str] = mapped_column(nullable=False)
    memory: Mapped[str] = mapped_column(nullable=False)
    disk: Mapped[str] = mapped_column(nullable=False)

    orders = relationship("UserOrder", back_populates="custom_image")

class UserOrder(Base):
    __tablename__ = 'user_orders'

    id: Mapped[int] = mapped_column(primary_key=True, unique=True, index=True)
    name: Mapped[str] = mapped_column(index=True, nullable=False)
    configuration: Mapped[dict] = mapped_column(JSON, nullable=False)
    network: Mapped[dict] = mapped_column(JSON,nullable=False)
    access: Mapped[dict] = mapped_column(JSON, nullable=False)
    cloud_ini: Mapped[dict] = mapped_column(JSON,nullable=False)

    image_id: Mapped[int | None] = mapped_column(ForeignKey('images.id'))
    custom_image_id: Mapped[int | None] = mapped_column(ForeignKey('custom_images.id'))
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'), nullable=False)

    user = relationship("User", back_populates="orders")
    image = relationship("Image", back_populates="orders")
    custom_image = relationship("CustomImage", back_populates="orders")

# create database
engine = create_engine('sqlite:///example.db', echo=False)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
