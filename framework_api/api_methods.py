import json
import os

import requests
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth

load_dotenv()
stepik_url = os.getenv('URL')
client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')


class StepikApi:
    def __init__(self):
        self.stepik_url = stepik_url

    def get_token(self):
        response = self.auth_oauth2_and_get_token(client_id, client_secret)
        return json.loads(response.text)['access_token']

    def auth_oauth2_and_get_token(self, client_id: str, client_secret: str):
        auth = HTTPBasicAuth(client_id, client_secret)
        response = requests.post(f'{self.stepik_url}/oauth2/token/',
                                 data={'grant_type': 'client_credentials'},
                                 auth=auth,
                                 allow_redirects=False)

        print(response.status_code)
        return response

    def logout(self):
        return requests.post(f'{self.stepik_url}/api/users/logout')

    def get_course_list(self, pagination_list_number: int):
        return requests.get(f'{self.stepik_url}/api/course-lists/{pagination_list_number}')

    def get_course_name(self, value: int) -> str:
        course_info = requests.get(f'{self.stepik_url}/api/courses/{value}')
        return course_info.json()['courses'][0]['title']

    def get_profile_info(self, profile_id: int):
        return requests.get(f'{self.stepik_url}/api/users/{profile_id}')

    def update_profile_info(self, profile_id: int, data: dict):
        return requests.put(f'{self.stepik_url}/api/profiles/{profile_id}',
                            headers={'Authorization': 'Bearer ' + self.get_token()}, json=data)


stepik_api = StepikApi()

