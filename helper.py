from faker import Faker
import data
import random
import string

class ChangeTestDataHelper:
    @staticmethod
    def modify_courier_body(key, value):
        body = data.TestDataCreateCourier.CREATE_COURIER_BODY.copy()
        body[key] = value

        return body

    @staticmethod
    def modify_create_color_body(color):
        body = data.TestDataCreateOrder.CREATE_ORDER_BODY.copy()
        body["color"] = [color]

        return body

class CourierFactory:
    @staticmethod
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    @staticmethod
    def courier_body_with_random_login_password_name():
        fake = Faker()

        body = {
            "login": CourierFactory.generate_random_string(10),
            "password": str(random.randint(100,999)),
            "firstName": fake.first_name()
        }
        return body