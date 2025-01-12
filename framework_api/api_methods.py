import json
import os

import allure
import requests
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth

from utils.utils import response_logging, response_attaching

load_dotenv()
stepik_url = os.getenv('URL')
client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')


class StepikApi:
    def __init__(self):
        self.stepik_url = stepik_url

    def get_token(self):
        with allure.step('Получение токена доступа'):
            response = self.auth_oauth2(client_id, client_secret)

            response_logging(response)
            response_attaching(response)
            return json.loads(response.text)['access_token']

    def auth_oauth2(self, client_id: str, client_secret: str):
        with allure.step('Проверка авторизации в системе'):
            auth = HTTPBasicAuth(client_id, client_secret)
            response = requests.post(f'{self.stepik_url}/oauth2/token/',
                                     data={'grant_type': 'client_credentials'},
                                     auth=auth,
                                     allow_redirects=False)
        response_logging(response)
        response_attaching(response)
        return response

    def logout(self):
        with allure.step('Выход из системы'):
            response = requests.post(f'{self.stepik_url}/api/users/logout')

            response_logging(response)
            response_attaching(response)

            return response

    def get_course_list(self, pagination_list_number: int):
        with allure.step(f'Получение списка курсов на странице {pagination_list_number}'):
            response = requests.get(f'{self.stepik_url}/api/course-lists/{pagination_list_number}')

            response_logging(response)
            response_attaching(response)

            return response

    def get_profile_info(self, profile_id: int):
        with allure.step(f'Получение информации о пользователе {profile_id}'):

            response = requests.get(f'{self.stepik_url}/api/users/{profile_id}')

            response_logging(response)
            response_attaching(response)

        return response

    def update_profile_info(self, profile_id: int, data: dict):
        with allure.step(f'Обновление информации о пользователе {profile_id}'):
            response = requests.put(f'{self.stepik_url}/api/profiles/{profile_id}',
                                headers={'Authorization': 'Bearer ' + self.get_token()}, json=data)

            # response_logging(response)
            # response_attaching(response)

            return response


stepik_api = StepikApi()