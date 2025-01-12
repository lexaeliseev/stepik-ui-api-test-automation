import allure

from framework_api import helper
from framework_api.api_methods import stepik_api
from resourses import CURRENT_DIR


@allure.label("owner", "aa.eliseev")
@allure.epic('AUTO')
@allure.feature('AUTO API')
@allure.story('Профиль пользователя')
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("Smoke")
@allure.title('Проверка получения информации о профиле пользователя')
def test_get_profile_info_success(reset_profile):
    profile_id = 1002719529

    response = stepik_api.get_profile_info(profile_id)

    with allure.step('Проверка на статус код'):
        assert response.status_code == 200

    result_json = response.json()
    helper.validate_json_schema(f'{CURRENT_DIR}/tests/api/users/schemas/user_profile_info_success.json', result_json)

    with allure.step('Проверка информации пользователя'):
        assert result_json['users'][0]['id'] == profile_id
        assert result_json['users'][0]['full_name'] == 'Тестовый аккаунт'


@allure.label("owner", "aa.eliseev")
@allure.epic('AUTO')
@allure.feature('AUTO API')
@allure.story('Профиль пользователя')
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("Smoke")
@allure.title('Проверка получения информации о несуществующем профиле пользователя')
def test_get_profile_info_not_found(reset_profile):
    profile_id = 'not_found'

    response = stepik_api.get_profile_info(profile_id)
    with allure.step('Проверка на статус код'):
        assert response.status_code == 404

    result_json = response.json()
    helper.validate_json_schema(f'{CURRENT_DIR}/tests/api/users/schemas/user_profile_info_not_found.json', result_json)

    with allure.step('Проверка текста от сервера'):
        assert result_json.get('detail') == 'Not found'
