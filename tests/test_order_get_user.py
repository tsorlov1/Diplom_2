import allure
from helpers.helpers_user import StellarBurgersApiUser
from data import ResponseText
class TestOrderGet:

    @allure.title('Получение заказов авторизованного пользователя')
    def test_get_order_success_authorization(self, registration_user_return_token):
        access_token = registration_user_return_token
        response = StellarBurgersApiUser.get_orders_user_success_authorization(access_token)
        assert response.status_code == 200 and ResponseText.text_success_true in response.text

    @allure.title('Получение заказов НЕавторизованного пользователя')
    def test_get_order_without_authorization(self):
        response = StellarBurgersApiUser.get_orders_user_without_authorization()
        assert response.status_code == 401 and response.text == ResponseText.text_get_order_without_authorization
