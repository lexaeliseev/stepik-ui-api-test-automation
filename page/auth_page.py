import time

import allure
from selene import browser, have, query, be


class AuthPage:
    pass

    def open_page(self):
        with allure.step("Открыть браузер"):
            browser.open('/')
            return self

    @staticmethod
    def click_menu_login():
        with allure.step("Клик по кнопке Войти"):
            browser.element('.navbar__auth_login').click()

    @staticmethod
    def auth_success(login, password):
        with allure.step(f"Ввести {login}"):
            browser.element('#id_login_email').should(be.blank).type(login)
        with allure.step(f"Ввести {password}"):
            browser.element('#id_login_password').should(be.blank).type(password)
        with allure.step('Нажать на кнопку Войти'):
            browser.element('.sign-form__btn').click()
        with allure.step('Проверка корректной авторизации пользователя'):
            browser.element('.navbar__auth_login').should(have.no.visible)
            browser.element('.navbar__profile-img').should(be.visible)

    @staticmethod
    def auth_failure(login, password):
        with allure.step(f"Ввести {login}"):
            browser.element('#id_login_email').should(be.blank).type(login)
        with allure.step(f"Ввести {password}"):
            browser.element('#id_login_password').should(be.blank).type(password)
        with allure.step('Нажать на кнопку Войти'):
            browser.element('.sign-form__btn').click()
        with allure.step('Отображение системной ошибки'):
            browser.element('.sign-form__messages').should(have.text('E-mail адрес и/или пароль не верны.'))


auth_page = AuthPage()