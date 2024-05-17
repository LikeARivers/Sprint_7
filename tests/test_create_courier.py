import allure
import data
import helper
import scooter_api
from conftest import random_courier_body, clean_created_random_courier

class TestCreateCourier:
    @allure.title("Проверка успешного создания курьера")
    @allure.description("Создание рандомного курьера с логином, паролем и именем, проверка статуса и тела ответа")
    def test_success_create_random_courier(self, random_courier_body, clean_created_random_courier):
        response_courier = scooter_api.ScooterApi.create_courier(random_courier_body)

        assert response_courier.status_code == 201 and response_courier.json()["ok"] == True


    @allure.title("Проверка ошибки при создании курьера с пустым логином")
    @allure.description("Создание шаблонного курьера с пустым логином, проверка статуса и тела ответа")
    def test_empty_login_create_courier(self):
        body = helper.ChangeTestDataHelper.modify_courier_body("login", "")
        created_courier_request = scooter_api.ScooterApi.create_courier(body)
        assert created_courier_request.status_code == 400 and created_courier_request.json()["message"] == "Недостаточно данных для создания учетной записи"

    @allure.title("Проверка ошибки при создании курьера с пустым паролем")
    @allure.description("Создание шаблонного курьера с пустым паролем, проверка статуса и тела ответа")
    def test_empty_password_create_courier(self):
        body = helper.ChangeTestDataHelper.modify_courier_body("password", "")
        created_courier_request = scooter_api.ScooterApi.create_courier(body)

        assert created_courier_request.status_code == 400 and created_courier_request.json()["message"] == "Недостаточно данных для создания учетной записи"

    @allure.title("Проверка ошибки при создании курьера без поля логин")
    @allure.description("Создание шаблонного курьера без поля логин, проверка статуса и тела ответа")
    def test_without_login_create_courier(self):
        body = data.TestDataCreateCourier.CREATE_COURIER_BODY_WITHOUT_LOGIN
        created_courier_request = scooter_api.ScooterApi.create_courier(body)
        assert created_courier_request.status_code == 400 and created_courier_request.json()[
            "message"] == "Недостаточно данных для создания учетной записи"

    @allure.title("Проверка ошибки при создании курьера без поля пароль")
    @allure.description("Создание шаблонного курьера без поля пароль, проверка статуса и тела ответа")
    def test_without_password_create_courier(self):
        body = data.TestDataCreateCourier.CREATE_COURIER_BODY_WITHOUT_PASSWORD
        created_courier_request = scooter_api.ScooterApi.create_courier(body)
        assert created_courier_request.status_code == 400 and created_courier_request.json()[
            "message"] == "Недостаточно данных для создания учетной записи"

    @allure.title("Проверка ошибки при создании двух одинаковых курьеров ")
    @allure.description("Создание двух шаблонных курьеров с одинаковым набором данных, проверка кода и статуса ответа")
    def test_two_create_courier(self, random_courier_body, clean_created_random_courier):
        response_courier_one = scooter_api.ScooterApi.create_courier(random_courier_body)
        response_courier_two = scooter_api.ScooterApi.create_courier(random_courier_body)
        assert response_courier_two.status_code == 409 and response_courier_two.json()[
            "message"] == "Этот логин уже используется"