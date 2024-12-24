import allure
from selene import browser, have, be


class AuthPage:
    pass

    @staticmethod
    def open_page():
        with allure.step("Открыть браузер"):
            browser.open('/')

    @staticmethod
    def click_menu_login():
        with allure.step("Клик по кнопке Войти для перехода в форму авторизации пользователя"):
            browser.element('.navbar__auth_login').click()

    @staticmethod
    def fill_login(login):
        with allure.step(f"Ввести {login} в форму авторизации"):
            browser.element('#id_login_email').should(be.blank).type(login)

    @staticmethod
    def fill_password(password):
        with allure.step(f"Ввести {password} в форму авторизации"):
            browser.element('#id_login_password').should(be.blank).type(password)

    @staticmethod
    def auth_click():
        with allure.step('Нажать на кнопку Войти в форме авторизации'):
            browser.element('.sign-form__btn').click()

    @staticmethod
    def click_user_menu(value: str):
        with allure.step(f"Перейти в меню: {value} пользователя"):
            browser.element('.navbar__profile-toggler').click()
            browser.all('.menu-item').element_by(have.text(value)).click()

    @staticmethod
    def check_success_auth(value: str):
        with allure.step('Проверка имени в личном кабинете пользователя'):
            browser.element('.profile__title').should(have.text(value))

    @staticmethod
    def check_success_logout():
        with allure.step('Проверка отображения формы регистрации при выходе из личного кабинета'):
            browser.element('//button[text()="OK"]').click()
            browser.element('[data-tab-name="login"]').should(be.visible)






    @staticmethod
    def auth_logout(login, password):
        with allure.step(f"Ввести {login}"):
            browser.element('#id_login_email').should(be.blank).type(login)
        with allure.step(f"Ввести {password}"):
            browser.element('#id_login_password').should(be.blank).type(password)
        with allure.step('Нажать на кнопку Войти'):
            browser.element('.sign-form__btn').click()
        with allure.step('Выйти из личного кабинета'):
            browser.element('.navbar__profile-img').click()
            browser.all('.ember-view').element_by(have.text('Выход')).click()
            browser.all('.modal-popup__footer').element_by(have.text('OK')).click()
        with allure.step('Проверка успешного выхода из личного кабинета'):
            browser.element('[data-tab-name="login"]').should(be.visible)


    @staticmethod
    def check_auth_failure():
        with allure.step('Отображение системной ошибки'):
            browser.element('.sign-form__messages').should(have.text('E-mail адрес и/или пароль не верны.'))


auth_page = AuthPage()