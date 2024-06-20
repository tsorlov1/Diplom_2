import requests
import allure
from data import ApiUrl


class StellarBurgersApiUser:
    @staticmethod
    @allure.step('Регистрация пользователя с рандомными данными')
    def registration_user_random(payload):
        response = requests.post(ApiUrl.API_URL_CREATE_USER, json=payload)
        return response

    @staticmethod
    @allure.step('Вход в систему')
    def login_user(payload):
        response = requests.post(ApiUrl.API_URL_LOGIN_USER, json=payload)
        return response

    @staticmethod
    @allure.step('Изменение данных авторизованного пользователя')
    def update_data_user_success_authorization(payload, access_token):
        response = requests.patch(ApiUrl.API_URL_UPDATE_USER_DATA, headers={'Authorization': access_token}, json=payload)
        return response

    @staticmethod
    @allure.step('Изменение данных НЕавторизованного пользователя')
    def update_data_user_without_authorization(payload):
        response = requests.patch(ApiUrl.API_URL_UPDATE_USER_DATA, json=payload)
        return response

    @staticmethod
    @allure.title('Получение заказов авторизованного пользователя')
    def get_orders_user_success_authorization(access_token):
        response = requests.get(ApiUrl.API_URL_GET_ORDERS, headers={'Authorization': access_token})
        return response

    @staticmethod
    @allure.title('Получение заказов НЕавторизованного пользователя')
    def get_orders_user_without_authorization():
        response = requests.get(ApiUrl.API_URL_GET_ORDERS, headers={'Authorization': ''})
        return response

    @staticmethod
    @allure.step('Удалить пользователя')
    def delete_user(access_token):
        response = requests.delete(ApiUrl.API_URL_DELETE_USER, headers={'Authorization': access_token})
        return response
