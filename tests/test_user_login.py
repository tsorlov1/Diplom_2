import allure
from data import ResponseText
from helpers.helpers_user import StellarBurgersApiUser


class TestUserLogin:

    @allure.title('Проверка успешной авторизации пользователя')
    def test_login_success(self, registration_user_return_log_pass):
        payload = registration_user_return_log_pass
        response = StellarBurgersApiUser.login_user(payload)
        assert response.status_code == 200 and ResponseText.text_success_true in response.text

    @allure.title('Проверка авторизации пользователя с неверным логином и/или паролем')
    def test_login_incorrect_login_or_password(self, registration_user_return_log_pass):
        payload = registration_user_return_log_pass
        email = f'{payload.get("email")}_'
        password = f'{payload.get("password")}_'
        payload = {"email": email,
                   "password": password}
        response = StellarBurgersApiUser.login_user(payload)
        assert response.status_code == 401 and response.text == ResponseText.text_incorrect_user_data
