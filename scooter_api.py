import allure
import requests
import urls

class ScooterApi:

    @staticmethod
    @allure.step("Отправка запроса на создание курьера")
    def create_courier(body):
        return requests.post(urls.BASE_URL + urls.CREATE_COURIER_ENDPOINT, json=body)

    @staticmethod
    @allure.step("Отправка запроса на авторизацию курьера")
    def auth_courier(body):
        return requests.post(urls.BASE_URL + urls.AUTH_ENDPOINT, json=body)

    @staticmethod
    @allure.step("Отправка запроса на удаление курьера")
    def delete_courier(courier_id):
        return requests.delete(urls.BASE_URL + urls.DELETE_COURIER_ENDPOINT + str(courier_id))

    @staticmethod
    @allure.step("Отправка запроса на создание заказа")
    def create_order(body):
        return requests.post(urls.BASE_URL + urls.CREATE_ORDER_ENDPOINT, json=body)

    @staticmethod
    @allure.step("Отправка запроса на получение списка заказов")
    def get_list_orders():
        return requests.get(urls.BASE_URL + urls.GET_LIST_ORDERS)
