import allure
import data
import helper
import scooter_api
from conftest import random_courier_body, clean_created_random_courier


class TestAuthCourier:
    @allure.title("Проверка успешной авторизации курьера")
    @allure.description("Авторизация рандомно созданного курьера с логином и паролем, проверка статуса и тела ответа")
    def test_success_auth_random_courier(self, random_courier_body, clean_created_random_courier):
        response_courier = scooter_api.ScooterApi.create_courier(random_courier_body)
        auth_courier_response = scooter_api.ScooterApi.auth_courier(random_courier_body)
        assert auth_courier_response.status_code == 200 and "id" in auth_courier_response.json()

    @allure.title("Проверка ошибки авторизации курьера")
    @allure.description("Авторизация курьера с пустым логином, проверка статуса и тела ответа")
    def test_auth_empty_login_courier(self):
        body = helper.ChangeTestDataHelper.modify_courier_body("login", "")
        auth_courier_response_empty_login = scooter_api.ScooterApi.auth_courier(body)
        assert auth_courier_response_empty_login.status_code == 400 and auth_courier_response_empty_login.json()[
            "message"] == "Недостаточно данных для входа"

    @allure.title("Проверка ошибки авторизации курьера")
    @allure.description("Авторизация курьера с пустым паролем, проверка статуса и тела ответа")
    def test_auth_empty_password_courier(self):
        body = helper.ChangeTestDataHelper.modify_courier_body("password", "")
        auth_courier_response_empty_password = scooter_api.ScooterApi.auth_courier(body)
        assert auth_courier_response_empty_password.status_code == 400 and auth_courier_response_empty_password.json()[
            "message"] == "Недостаточно данных для входа"
    @allure.title("Проверка ошибки авторизации курьера")
    @allure.description("Авторизация курьера без поля логин, проверка статуса и тела ответа")
    def test_auth_without_login_courier(self):
        body = data.TestDataAuthorization.AUTH_COURIER_BODY_WITHOUT_LOGIN
        auth_courier_response_without_login = scooter_api.ScooterApi.auth_courier(body)
        assert auth_courier_response_without_login.status_code == 400 and auth_courier_response_without_login.json()[
            "message"] == "Недостаточно данных для входа"

    @allure.title("Проверка ошибки при авторизации несуществующего курьера")
    @allure.description("Авторизация несуществующего курьера, проверка статуса и тела ответа")
    def test_auth_nonexistent_courier(self):
        body = data.TestDataAuthorization.AUTHORIZATION_NONEXISTENT_COURIER_BODY
        created_courier_request = scooter_api.ScooterApi.auth_courier(body)
        assert created_courier_request.status_code == 404 and created_courier_request.json()["message"] == "Учетная запись не найдена"
