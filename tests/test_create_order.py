import allure
import pytest
import helper
import scooter_api
from conftest import clean_created_orders



class TestCreateOrder:
    @allure.title("Проверка успешного создания заказа")
    @allure.description("Создание шаблонных заказов разных цветов, проверка статуса и наличия track в ответе")
    @pytest.mark.parametrize("color", ["BLACK", "GRAY", "BLACK GRAY", ""])
    def test_success_create_order(self, color, clean_created_orders):
        body = helper.ChangeTestDataHelper.modify_create_color_body(color)
        created_order_request = scooter_api.ScooterApi.create_order(body)

        assert created_order_request.status_code == 201 and "track" in created_order_request.json() is not None

    @allure.title("Проверка успешного получения списка заказов")
    @allure.description("Получение списка заказов, проверка кода и тела ответа")
    def test_success_get_list_order(self):
        get_list_orders = scooter_api.ScooterApi.get_list_orders()

        assert get_list_orders.status_code == 200 and "orders" in get_list_orders.json()
