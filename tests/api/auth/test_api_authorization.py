import os
import allure

from utils import helper
from framework_api.api_methods import stepik_api
from resourses import CURRENT_DIR

client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')


@allure.label("owner", "aa.eliseev")
@allure.epic('AUTO')
@allure.feature('AUTO API')
@allure.story('Авторизация')
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("Smoke")
@allure.title('Успешная авторизация в системе')
def test_auth_success():
    result = stepik_api.auth_oauth2(client_id, client_secret)
    assert result.status_code == 200

    result_json = result.json()
    helper.validate_json_schema(f'{CURRENT_DIR}/tests/api/auth/schemas/auth_success_schema.json', result_json)


@allure.label("owner", "aa.eliseev")
@allure.epic('AUTO')
@allure.feature('AUTO API')
@allure.story('Авторизация')
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("Smoke")
@allure.title('Попытка входа в систему с неверными данными')
def test_auth_failure():
    result = stepik_api.auth_oauth2(client_id, 'bad_client_secret')

    with allure.step('Проверка ответа на статус-код'):
        assert result.status_code == 401

    result_json = result.json()
    helper.validate_json_schema(f'{CURRENT_DIR}/tests/api/auth/schemas/auth_failure_schema.json', result_json)

    with allure.step('Проверка текста ответа'):
        assert result_json.get('error') == 'invalid_client'


@allure.label("owner", "aa.eliseev")
@allure.epic('AUTO')
@allure.feature('AUTO API')
@allure.story('Авторизация')
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("Smoke")
@allure.title('Выход пользователя из системы')
def test_auth_logout(auth_fixture):
    response = stepik_api.logout()
    assert response.status_code == 401

    result_json = response.json()
    helper.validate_json_schema(f'{CURRENT_DIR}/tests/api/auth/schemas/auth_logout_schema.json', result_json)
    assert result_json.get('detail') == 'CSRF Failed: Referer checking failed - no Referer.'
