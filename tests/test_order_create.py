import allure
from data import Ingredient
from data import ResponseText
from helpers.helpers_order import StellarBurgersApiOrder


class TestOrderCreate:

    @allure.title('Создание заказа авторизованным пользователем')
    def test_create_order_success_authorization(self, registration_user_return_token):
        access_token = registration_user_return_token
        payload = Ingredient.correct_ingredients_data
        response = StellarBurgersApiOrder.create_order_success_authorization(access_token, payload)
        assert response.status_code == 200 and ResponseText.text_success_true in response.text

    @allure.title('Создание заказа НЕавторизованным пользователем')
    def test_create_order_without_authorization(self):
        payload = Ingredient.correct_ingredients_data
        response = StellarBurgersApiOrder.create_order_without_authorization(payload)
        assert response.status_code == 200 and ResponseText.text_success_true in response.text

    @allure.title('Создание заказа без указания ингредиента')
    def test_create_order_without_ingredients(self):
        payload = Ingredient.without_ingredients_data
        response = StellarBurgersApiOrder.create_order_without_authorization(payload)
        assert response.status_code == 400 and response.text == ResponseText.text_order_without_ingredients

    @allure.title('Создание заказа с неверным хешем ингредиента')
    def test_create_order_incorrect_hash_ingredients(self):
        payload = Ingredient.incorrect_ingredients_data
        response = StellarBurgersApiOrder.create_order_without_authorization(payload)
        assert response.status_code == 500
