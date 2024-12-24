import os
import allure
from page.auth_page import auth_page


@allure.label("owner", "aa.eliseev")
@allure.epic('UI')
@allure.feature('Авторизация')
@allure.tag("Smoke")
@allure.title('Успешная авторизация в системе')
def test_auth_success(setup_browser):
    auth_page.open_page()
    auth_page.click_menu_login()
    auth_page.fill_login(os.getenv('STEPIK_EMAIL'))
    auth_page.fill_password(os.getenv('STEPIK_PASSWORD'))
    auth_page.auth_click()
    auth_page.click_user_menu('Профиль')
    auth_page.check_success_auth('Тестовый аккаунт')


@allure.label("owner", "aa.eliseev")
@allure.epic('UI')
@allure.feature('Авторизация')
@allure.tag("Smoke")
@allure.title('Выход авторизованного пользователя из системы')
def test_auth_logout(setup_browser):

    # заменить этот блок апишной авторизацией
    auth_page.open_page()
    auth_page.click_menu_login()
    auth_page.fill_login(os.getenv('STEPIK_EMAIL'))
    auth_page.fill_password(os.getenv('STEPIK_PASSWORD'))
    auth_page.auth_click()

    auth_page.click_user_menu('Профиль')
    auth_page.check_success_auth('Тестовый аккаунт')

    auth_page.click_user_menu('Выход')
    auth_page.check_success_logout()


@allure.label("owner", "aa.eliseev")
@allure.epic('UI')
@allure.feature('Авторизация')
@allure.tag("Smoke")
@allure.title('Авторизация с невалидными данными')
def test_auth_failure(setup_browser):
    auth_page.open_page()
    auth_page.click_menu_login()
    auth_page.fill_login('login@test.com')
    auth_page.fill_password('password')
    auth_page.auth_click()
    auth_page.check_auth_failure()