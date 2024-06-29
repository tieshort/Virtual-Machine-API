from dataBase import Session, engine
from createToDataBase import create_user, create_image, create_user_order

# create session
db_session = Session(bind=engine)

# Example
user_data = {
    "name": "йкйкйкй",
    "password": "кйкйцкйайа",
    "email": "sdfdsfs.sfsfdsfs@example.com*/*", #unique value
    "phone": "+12348888890"
}

image_data = {
    "name": "Image1_1",
    "operating_system": "Linuxxxxx",
    "memory": 8096,
    "disk": 400
}

user_order_data = {
    "name": "Order1_1",
    "image_id": 1,
    "configuration": {"config": "value1.1"},
    "network": {"network": "value1.1"},
    "access": {"access": "value1.1"},
    "cloud_ini": {"cloud": "value1.1"},
    "user_id": 1
}

created_user = create_user(db_session, user_data)
created_image = create_image(db_session, image_data)
created_user_order = create_user_order(db_session, user_order_data)

# check
print(f"user with an id {created_user.id} has been created")
print(f"image with an id {created_image.id} has been created")
print(f"order has been created by a user with an id {created_user_order.id}")

# close session
db_session.close()
