import os
import allure
from framework_ui.page.auth_page import auth_page


@allure.label("owner", "aa.eliseev")
@allure.feature('Авторизация')
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("Smoke")
@allure.title('Успешная авторизация в системе и выход из системы')
@allure.story('UI')
def test_auth_and_logout_success(setup_browser):
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
@allure.feature('Авторизация')
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("Smoke")
@allure.title('Авторизация с невалидными данными')
@allure.story('AUTO')
@allure.story('UI')
def test_auth_failure(setup_browser):
    auth_page.open_page()
    auth_page.click_menu_login()
    auth_page.fill_login('login@test.com')
    auth_page.fill_password('password')
    auth_page.auth_click()
    auth_page.check_auth_failure()