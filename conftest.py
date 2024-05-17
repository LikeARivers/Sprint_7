import allure
import pytest
import scooter_api
import helper

@allure.step("Генерация рандомного тела курьера")
@pytest.fixture(scope='function')
def random_courier_body():
    return helper.CourierFactory.courier_body_with_random_login_password_name()

@allure.step("Получение id и удаление рандомного курьера")
@pytest.fixture(scope='function')
def clean_created_random_courier(random_courier_body):
    yield
    auth_response = scooter_api.ScooterApi.auth_courier(random_courier_body)
    courier_id = auth_response.json().get("id")
    delete_response = scooter_api.ScooterApi.delete_courier(courier_id)
