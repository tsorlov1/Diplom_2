import faker

class User:
    @staticmethod
    def user_random():
        fake = faker.Faker()
        user_data_random = {
            'email': fake.email(),
            'password': fake.password(),
            'name': fake.name()
        }
        return user_data_random

class ApiUrl:
    API_URL = 'https://stellarburgers.nomoreparties.site/'
    API_URL_CREATE_USER = f'{API_URL}api/auth/register'
    API_URL_LOGIN_USER = f'{API_URL}api/auth/login'
    API_URL_UPDATE_USER_DATA = f'{API_URL}api/auth/user'
    API_URL_DELETE_USER = f'{API_URL}api/auth/user'
    API_URL_CREATE_ORDER = f'{API_URL}api/orders'
    API_URL_GET_ORDERS = f'{API_URL}api/orders'

class Ingredient:
    correct_ingredients_data = {
        "ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa70"]}
    incorrect_ingredients_data = {
        "ingredients": ["61c0c5a71d1f82001bdaaa6da", "61c0c5a71d1f82001bdaaa70d"]}
    without_ingredients_data = {"ingredients": []}



class ResponseText:
    text_success_true = '"success":true'
    text_incorrect_user_data = '{"success":false,"message":"email or password are incorrect"}'
    text_registration_insufficient_data = '{"success":false,"message":"Email, password and name are required fields"}'
    text_user_update_data_without_authorization = '{"success":false,"message":"You should be authorised"}'
    text_order_without_ingredients = '{"success":false,"message":"Ingredient ids must be provided"}'
    text_get_order_without_authorization = '{"success":false,"message":"You should be authorised"}'
