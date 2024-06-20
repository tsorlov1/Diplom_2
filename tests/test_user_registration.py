import pytest
import requests
import allure
from data import ApiUrl, ResponseText


class TestUserRegistration:
    @allure.title('Проверка успешной регистрации пользователя')
    def test_user_success_registration(self, registration_user_return_response):
        response = registration_user_return_response
        assert response.status_code == 200 and response.json().get('success')

    @allure.title('Проверка ошибки при создания пользователя с уже существующим логином')
    def test_user_registration_double_login(self, registration_user_return_log_pass):
        payload = registration_user_return_log_pass
        response = requests.post(ApiUrl.API_URL_CREATE_USER, json=payload)
        assert response.status_code == 403 and response.text == '{"success":false,"message":"User already exists"}'

    @allure.title('Проверка ввода обязательных полей при регистрации пользователя')
    @pytest.mark.parametrize(
        "payload",
        [
            {'email': 'korneeva250667@gmail.com', 'password': '1234', 'name': ''},
            {'email': 'korneeva250667@gmail.com', 'password': '', 'name': 'Татьяна'},
            {'email': '', 'password': '1234', 'name': 'Татьяна'}
        ])
    def test_user_registration_required_field(self, payload):
        response = requests.post(ApiUrl.API_URL_CREATE_USER, json=payload)
        assert response.status_code == 403 and response.text == ResponseText.text_registration_insufficient_data
