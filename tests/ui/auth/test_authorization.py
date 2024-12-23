import os

import allure
import pytest
from dotenv import load_dotenv

from page.auth_page import auth_page



@allure.label("owner", "aa.eliseev")
@allure.feature('Поиск')
@allure.tag("Smoke")
@allure.title('Успешная авторизация в системе')
def test_auth_success(setup_browser):
    auth_page.open_page()
    auth_page.click_menu_login()
    auth_page.auth_success(os.getenv('STEPIK_EMAIL'), os.getenv('STEPIK_PASSWORD'))


@pytest.mark.parametrize(
    'login, password',
    [(os.getenv('STEPIK_EMAIL'), 'password'),
     ('login@test.com', os.getenv('STEPIK_PASSWORD'))],
    ids=['Login1', 'Login2'])
@allure.label("owner", "aa.eliseev")
@allure.feature('Поиск')
@allure.tag("Smoke")
@allure.title('Авторизация с невалидными данными')
def test_auth_failure(setup_browser, login, password):
    load_dotenv()
    auth_page.open_page()
    auth_page.click_menu_login()
    auth_page.auth_failure(login, password)
