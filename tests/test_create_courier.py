import allure
import helper
import scooter_api
from conftest import random_courier, two_courier, create_missing_name_courier

class TestCreateCourier:
    @allure.title("Проверка успешного создания курьера")
    @allure.description("Создание рандомного курьера с логином, паролем и именем, проверка статуса и тела ответа")
    def test_success_create_random_courier(self, random_courier):
        response_courier = random_courier
        assert response_courier.status_code == 201 and response_courier.json()["ok"] == True

    @allure.title("Проверка ошибки при создании курьера с пустым логином")
    @allure.description("Создание шаблонного курьера с пустым логином, проверка статуса и тела ответа")
    def test_empty_login_create_courier(self):
        body = helper.ChangeTestDataHelper.modify_create_courier_body("login", "")
        created_courier_request = scooter_api.ScooterApi.create_courier(body)
        assert created_courier_request.status_code == 400 and created_courier_request.json()["message"] == "Недостаточно данных для создания учетной записи"

    @allure.title("Проверка ошибки при создании курьера с пустым паролем")
    @allure.description("Создание шаблонного курьера с пустым паролем, проверка статуса и тела ответа")
    def test_empty_password_create_courier(self):
        body = helper.ChangeTestDataHelper.modify_create_courier_body("password", "")
        created_courier_request = scooter_api.ScooterApi.create_courier(body)

        assert created_courier_request.status_code == 400 and created_courier_request.json()["message"] == "Недостаточно данных для создания учетной записи"

    @allure.title("Проверка ошибки при создании курьера с пустым именем")
    @allure.description("Создание шаблонного курьера с пустым именем, проверка статуса и тела ответа")
    def test_empty_first_name_create_courier(self, create_missing_name_courier):
        created_courier_request = create_missing_name_courier

        assert created_courier_request.status_code == 400 and created_courier_request.json()["message"] == "Недостаточно данных для создания учетной записи"

    @allure.title("Проверка ошибки при создании двух одинаковых курьеров ")
    @allure.description("Создание двух шаблонных курьеров с одинаковым набором данных, проверка кода и статуса ответа")
    def test_two_create_courier(self, two_courier):
        created_two_courier_request = two_courier

        assert created_two_courier_request.status_code == 409 and created_two_courier_request.json()["message"] == "Этот логин уже используется"
