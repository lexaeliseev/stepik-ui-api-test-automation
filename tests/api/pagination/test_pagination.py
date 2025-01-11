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
@allure.feature('')
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("Smoke")
@allure.title('')
def test_auth_success():
    result = stepik_api.auth_oauth2(client_id, client_secret)

    assert result.status_code == 200

    response_logging(result)
    response_attaching(result)

    course_list_number = 355
    result = stepik_api.get_course_list(course_list_number)
    result_json = result.json()

    response_logging(result)
    response_attaching(result)

    assert result.status_code == 200
    helper.validate_json_schema(f'{CURRENT_DIR}/tests/api/pagination/schemas/pagination_schema.json', result_json)
    assert result_json['course-lists'][0]['id'] == course_list_number
    assert result_json['course-lists'][0]['title'] == 'Программирование для детей'




