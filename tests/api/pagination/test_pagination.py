import os

import allure

from framework_api import helper
from framework_api.api_methods import stepik_api
from resourses import CURRENT_DIR

client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')


@allure.label("owner", "aa.eliseev")
@allure.epic('API')
@allure.feature('Пагинация')
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("Smoke")
@allure.title('Проверка корректной пагинации')
@allure.label('API')
def test_auth_success():
    course_list_number = 355
    result = stepik_api.get_course_list(course_list_number)
    assert result.status_code == 200

    result_json = result.json()
    helper.validate_json_schema(f'{CURRENT_DIR}/tests/api/pagination/schemas/pagination_success_schema.json',
                                result_json)
    assert result_json['course-lists'][0]['id'] == course_list_number
    assert result_json['course-lists'][0]['title'] == 'Программирование для детей'


@allure.label("owner", "aa.eliseev")
@allure.epic('API')
@allure.feature('Пагинация')
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("Smoke")
@allure.title('Проверка отображения ошибки при переходе на несуществующую страницу')
@allure.label('API')
def test_auth_success():
    course_list_number = 355000
    result = stepik_api.get_course_list(course_list_number)
    assert result.status_code == 404

    result_json = result.json()
    helper.validate_json_schema(f'{CURRENT_DIR}/tests/api/pagination/schemas/pagination_not_found_schema.json',
                                result_json)