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
@allure.story('Пагинация')
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("Smoke")
@allure.title('Проверка успешного получения списка курсов')
def test_get_course_list_success():
    course_list_number = 355
    result = stepik_api.get_course_list(course_list_number)

    with allure.step('Проверка ответа на статус-код'):
        assert result.status_code == 200

    result_json = result.json()
    helper.validate_json_schema(f'{CURRENT_DIR}/tests/api/course_lists/schemas/pagination_success_schema.json',
                                result_json)
    with allure.step('Проверка корректного перехода на страницу курса'):
        assert result_json['course-lists'][0]['id'] == course_list_number
        assert result_json['course-lists'][0]['title'] == 'Программирование для детей'


@allure.label("owner", "aa.eliseev")
@allure.epic('AUTO')
@allure.feature('AUTO API')
@allure.story('Пагинация')
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("Smoke")
@allure.title('Проверка ответа при запросе несуществующего списка курсов')
def test_get_course_list_not_found():
    course_list_number = 355000

    result = stepik_api.get_course_list(course_list_number)

    with allure.step('Проверка ответа на статус-код'):
        assert result.status_code == 404

    result_json = result.json()
    helper.validate_json_schema(f'{CURRENT_DIR}/tests/api/course_lists/schemas/pagination_not_found_schema.json',
                                result_json)

    with allure.step('Проверка текста ответа'):
        assert result_json.get('detail') == 'Not found'
