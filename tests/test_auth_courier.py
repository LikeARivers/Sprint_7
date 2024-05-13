import allure
import data
import scooter_api
from conftest import auth_random_courier, auth_empty_login_courier, auth_empty_password_courier


class TestAuthCourier:
    @allure.title("Проверка успешной авторизации курьера")
    @allure.description("Авторизация рандомно созданного курьера с логином и паролем, проверка статуса и тела ответа")
    def test_success_auth_random_courier(self, auth_random_courier):
        response_courier = auth_random_courier
        assert response_courier.status_code == 200 and "id" in response_courier.json()

    @allure.title("Проверка ошибки авторизации курьера")
    @allure.description("Авторизация курьера с пустым логином, проверка статуса и тела ответа")
    def test_auth_empty_login_courier(self, auth_empty_login_courier):
        response_courier = auth_empty_login_courier
        assert response_courier.status_code == 400 and response_courier.json()["message"] == "Недостаточно данных для входа"

    @allure.title("Проверка ошибки авторизации курьера")
    @allure.description("Авторизация курьера с пустым паролем, проверка статуса и тела ответа")
    def test_auth_empty_password_courier(self, auth_empty_password_courier):
        response_courier = auth_empty_password_courier
        assert response_courier.status_code == 400 and response_courier.json()["message"] == "Недостаточно данных для входа"

    @allure.title("Проверка ошибки при авторизации несуществующего курьера")
    @allure.description("Авторизация несуществующего курьера, проверка статуса и тела ответа")
    def test_auth_nonexistent_courier(self):
        body = data.TestDataAuthorization.AUTHORIZATION_NONEXISTENT_COURIER_BODY
        created_courier_request = scooter_api.ScooterApi.auth_courier(body)
        assert created_courier_request.status_code == 404 and created_courier_request.json()["message"] == "Учетная запись не найдена"
