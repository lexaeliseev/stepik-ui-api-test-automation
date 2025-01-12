import copy
import os

import allure
import pytest
from framework_api.api_methods import stepik_api
from tests.api.users.data.user_data import user_data

client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')


@pytest.fixture(scope='function')
@allure.step('Авторизация пользователя через API')
def auth_fixture():
    response = stepik_api.auth_oauth2(client_id, client_secret)
    assert response.status_code == 200
    return response


@pytest.fixture(scope="function")
def reset_profile():
    original_data = copy.deepcopy(user_data)

    yield

    response = stepik_api.update_profile_info(1002719529, original_data)
    assert response.status_code == 200, f"Failed to reset profile: {response.json()}"