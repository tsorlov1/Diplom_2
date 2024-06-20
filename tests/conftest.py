import pytest
from data import User
from helpers.helpers_user import StellarBurgersApiUser


@pytest.fixture
def registration_user_return_response():
    payload = User.user_random()
    response = StellarBurgersApiUser.registration_user_random(payload)
    yield response
    access_token = response.json()['accessToken']
    StellarBurgersApiUser.delete_user(access_token)


@pytest.fixture
def registration_user_return_log_pass():
    payload = User.user_random()
    response = StellarBurgersApiUser.registration_user_random(payload)
    yield payload
    access_token = response.json()['accessToken']
    StellarBurgersApiUser.delete_user(access_token)


@pytest.fixture
def registration_user_return_token():
    payload = User.user_random()
    response = StellarBurgersApiUser.registration_user_random(payload)
    access_token = response.json()['accessToken']
    yield access_token
    StellarBurgersApiUser.delete_user(access_token)
