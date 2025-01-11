import os

import allure

from framework_api import helper
from framework_api.api_methods import stepik_api
from resourses import CURRENT_DIR
from utils.utils import response_logging, response_attaching

client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')


@allure.label("owner", "aa.eliseev")
@allure.epic('API')
@allure.feature('Авторизация')
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("Smoke")
@allure.title('Авторизация в системе с валидными данными')
def test_auth_success():
    result = stepik_api.auth_oauth2(client_id, client_secret)

    assert result.status_code == 200

    # response_logging(result)
    # response_attaching(result)

    result_json = result.json()
    helper.validate_json_schema(f'{CURRENT_DIR}/tests/api/auth/schemas/auth_success_schema.json', result_json)


@allure.label("owner", "aa.eliseev")
@allure.epic('API')
@allure.feature('Авторизация')
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("Smoke")
@allure.title('Авторизация в системе с невалидными данными')
def test_auth_failure():
    result = stepik_api.auth_oauth2(client_id, 'bad_client_secret')
    assert result.status_code == 401

    # response_logging(result)
    # response_attaching(result)

    result_json = result.json()
    helper.validate_json_schema(f'{CURRENT_DIR}/tests/api/auth/schemas/auth_failure_schema.json', result_json)
