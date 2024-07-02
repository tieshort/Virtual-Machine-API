from models import Session, engine, CustomImage
from createToDataBase import create_user, create_image, create_custom_image, create_user_order, get_user_info

# create session
db_session = Session(bind=engine)

# Example
user_data = {
    "name": "gsdgdsgds",
    "password": "sgddsgdsgd",
    "email": "sdfdsfs.sfsfdsfs@******/**example.com", #unique value
    "phone": "+5616516222231265222"
}

# image_data = {
#     "name": "Image1_1",
#     "operating_system": "Linuxxxxx",
#     "memory": "8096",
#     "disk": "400"
# }

#custom_image_data = {
image_data = {
    "name": "Image1_1",
    "load_file": "C:\Lib\help",
    "user_id": "2",
    "operating_system": "Linuxxxxx",
    "memory": "8096",
    "disk": "400"
}

user_order_data = {
    "name": "Order1_1",
    "image_id": None,
    "custom_image_id": 5,
    "configuration": {"config": "value1.1"},
    "network": {"network": "value1.1"},
    "access": {"access": "value1.1"},
    "cloud_ini": {"cloud": "value1.1"},
    "user_id": 2
}

created_user = create_user(db_session, user_data)
#created_image = create_image(db_session, image_data)
created_custom_image = create_custom_image(db_session, image_data)
created_user_order = create_user_order(db_session, user_order_data)

# check
print(f"user with an id {created_user.id} has been created")
#print(f"image with an id {created_image.id} has been created")
print(f"custom image with an id {created_custom_image.id} has been created")
print(f"order has been created by a user with an id {created_user_order.id}")

# Get and print user with orders and images
user_id = 2
user_data = get_user_info(db_session, user_id)
if user_data:
    user = user_data["user"]
    print(f"User with ID {user_id} found: {user.name}, {user.email}, {user.phone}")
    for order_with_image in user_data["orders_with_images"]:
        order = order_with_image["order"]
        image = order_with_image["image"]
        print(f"Order ID: {order.id}, Order Name: {order.name}, configuration: {order.configuration}, Network: {order.network}")
        if order.custom_image_id is not None:
            custom_image = db_session.query(CustomImage).filter(CustomImage.id == order.custom_image_id).first()
            if custom_image:
                print(
                    f"Custom Image ID: {custom_image.id}, Custom Image Name: {custom_image.name}, OS: {custom_image.operating_system}")
        else:
            if image:
                print(f"Image ID: {image.id}, Image Name: {image.name}, OS: {image.operating_system}")


else:
    print(f"User with ID {user_id} not found")

# close session
db_session.close()
