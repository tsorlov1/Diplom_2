import allure
from data import User, ResponseText
from helpers.helpers_user import StellarBurgersApiUser

class TestUserUpdateData:

    @allure.title('Изменение данных пользователя с авторизацией')
    def test_user_update_data_success_authorization(self, registration_user_return_token):
        access_token = registration_user_return_token
        payload = User.user_random()
        response = StellarBurgersApiUser.update_data_user_success_authorization(payload, access_token)
        assert response.status_code == 200 and ResponseText.text_success_true in response.text

    @allure.title('Изменение данных пользователя без авторизации')
    def test_user_update_data_without_authorization(self):
        payload = User.user_random()
        response = StellarBurgersApiUser.update_data_user_without_authorization(payload)
        assert response.status_code == 401 and response.text == ResponseText.text_user_update_data_without_authorization
