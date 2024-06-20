import requests
import allure
from data import ApiUrl


class StellarBurgersApiOrder:
    @staticmethod
    @allure.step('Создание заказа авторизованным пользователем')
    def create_order_success_authorization(access_token, payload):
        response = requests.post(ApiUrl.API_URL_CREATE_ORDER, headers={'Authorization': access_token}, json=payload)
        return response

    @staticmethod
    @allure.step('Создание заказа НЕавторизованным пользователем')
    def create_order_without_authorization(payload):
        response = requests.post(ApiUrl.API_URL_CREATE_ORDER, json=payload)
        return response
