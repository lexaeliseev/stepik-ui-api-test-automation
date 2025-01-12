import copy
import allure

from framework_api import helper
from framework_api.api_methods import stepik_api
from resourses import CURRENT_DIR
from tests.api.data.user_data import user_data


@allure.label("owner", "aa.eliseev")
@allure.epic('AUTO')
@allure.feature('AUTO API')
@allure.story('Профиль пользователя')
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("Smoke")
@allure.title('Обновление информации профиля пользователя')
def test_update_profile_info_success(reset_profile):
    profile_id = 1002719529
    first_name = 'Update'
    last_name = 'name'
    data = copy.deepcopy(user_data)
    data['profile']['first_name'] = first_name
    data['profile']['last_name'] = last_name

    response = stepik_api.update_profile_info(profile_id, data)

    result_json = response.json()
    with allure.step('Проверка на статус код'):
        assert response.status_code == 200

    with allure.step('Проверка успешного обновления информации профиля'):
        assert result_json['profiles'][0]['full_name'] == 'Update name'

    helper.validate_json_schema(f'{CURRENT_DIR}/tests/api/users/schemas/user_update_profile_info.json',
                                result_json)