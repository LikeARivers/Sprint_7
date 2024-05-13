import allure
import pytest
import requests
import data
import scooter_api
import helper
import urls


@allure.step("СОЗДАНИЕ, авторизация, удаление рандомного курьера курьера")
@pytest.fixture(scope='function')
def random_courier():
    courier_body = helper.CourierFactory.courier_body_with_random_login_password_name()
    courier_create = scooter_api.ScooterApi.create_courier(courier_body)
    yield courier_create
    auth_courier_response = scooter_api.ScooterApi.auth_courier(courier_body)
    courier_id = auth_courier_response.json().get("id")
    delete_courier_response = requests.delete(f"{urls.BASE_URL}{urls.DELETE_COURIER_ENDPOINT}{courier_id}")

@allure.step("Создание двух одинаковых курьеров, авторизация, удаление")
@pytest.fixture(scope='function')
def two_courier():
    courier_body = data.TestDataCreateCourier.CREATE_IDENTICAL_COURIER_BODY
    courier_create_response_one = scooter_api.ScooterApi.create_courier(courier_body)
    courier_create_response_two = scooter_api.ScooterApi.create_courier(courier_body)
    yield courier_create_response_two
    auth_courier_response = scooter_api.ScooterApi.auth_courier(courier_body)
    courier_id = auth_courier_response.json().get("id")
    delete_courier_response = requests.delete(f"{urls.BASE_URL}{urls.DELETE_COURIER_ENDPOINT}{courier_id}")

@allure.step("Создание курьера с пустым именем, авторизация, удаление")
@pytest.fixture(scope='function')
def create_missing_name_courier():
    body = helper.ChangeTestDataHelper.modify_create_courier_body("firstName", "")
    created_courier = scooter_api.ScooterApi.create_courier(body)
    yield created_courier
    auth_courier_response = scooter_api.ScooterApi.auth_courier(body)
    courier_id = auth_courier_response.json().get("id")
    delete_courier_response = requests.delete(f"{urls.BASE_URL}{urls.DELETE_COURIER_ENDPOINT}{courier_id}")

@allure.step("Создание, АВТОРИЗАЦИЯ, удаление рандомного курьера")
@pytest.fixture(scope='function')
def auth_random_courier():
    courier_body = helper.CourierFactory.courier_body_with_random_login_password_name()
    courier_create_response = scooter_api.ScooterApi.create_courier(courier_body)
    auth_courier_response = scooter_api.ScooterApi.auth_courier(courier_body)
    yield auth_courier_response
    courier_id = auth_courier_response.json().get("id")
    delete_courier_response = requests.delete(f"{urls.BASE_URL}{urls.DELETE_COURIER_ENDPOINT}{courier_id}")

@allure.step("Создание, АВТОРИЗАЦИЯ с пустым логином, удаление курьера")
@pytest.fixture(scope='function')
def auth_empty_login_courier():
    courier_body = data.TestDataCreateCourier.CREATE_COURIER_BODY
    courier_create_response = scooter_api.ScooterApi.create_courier(courier_body)
    empty_login_body = courier_body.copy()
    empty_login_body["login"] = ""
    auth_courier_response_empty_login = scooter_api.ScooterApi.auth_courier(empty_login_body)
    yield auth_courier_response_empty_login
    auth_courier_response = scooter_api.ScooterApi.auth_courier(courier_body)
    courier_id = auth_courier_response.json().get("id")
    delete_courier_response = requests.delete(f"{urls.BASE_URL}{urls.DELETE_COURIER_ENDPOINT}{courier_id}")

@allure.step("Создание, АВТОРИЗАЦИЯ с пустым паролем, удаление курьера")
@pytest.fixture(scope='function')
def auth_empty_password_courier():
    courier_body = data.TestDataCreateCourier.CREATE_COURIER_BODY
    courier_create_response = scooter_api.ScooterApi.create_courier(courier_body)
    empty_login_body = courier_body.copy()
    empty_login_body["password"] = ""
    auth_courier_response_empty_login = scooter_api.ScooterApi.auth_courier(empty_login_body)
    yield auth_courier_response_empty_login
    auth_courier_response = scooter_api.ScooterApi.auth_courier(courier_body)
    courier_id = auth_courier_response.json().get("id")
    delete_courier_response = requests.delete(f"{urls.BASE_URL}{urls.DELETE_COURIER_ENDPOINT}{courier_id}")


@pytest.fixture(scope="function")#удаление заказов
def clean_created_orders():
    orders = scooter_api.ScooterApi.get_list_orders().json().get("orders", [])
    tracks = [order["track"] for order in orders]
    yield
    for track in tracks:
        scooter_api.ScooterApi.delete_order_by_track(track)