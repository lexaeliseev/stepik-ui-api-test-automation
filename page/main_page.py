import allure
from selene import browser, have, be


class MainPage:

    def open_page(self):
        with allure.step("Открыть браузер"):
            browser.open('/')
            return self

    """ ПОИСК """

    @staticmethod
    def get_search_item_success():
        with allure.step("Получить список значений для поиска"):
            return [
                ('"Поколение Python": курс для начинающих', '"Python Generation": a course for beginner"'),
                ('Интерактивный тренажер по SQL', 'Interactive SQL Trainer')
            ]

    @staticmethod
    def get_search_item_failure():
        with allure.step("Получить список значений для неуспешного поиска"):
            return [
                ('test test test test test', 'test test test test test'),
                ('нененнеос', 'nenenneos')
            ]

    @staticmethod
    def search_success(value):
        with allure.step(f"Поиск по значению {value}"):
            browser.element('.search-form__input ').type(value).press_enter()

        with allure.step(f"Проверка корректного поиска по значению {value}"):
            browser.element('.course-card__title').should(have.text(value))

    @staticmethod
    def search_failure(value):
        with allure.step(f"Поиск по значению {value}"):
            browser.element('.search-form__input ').type(value).press_enter()

        with allure.step("Проверка отображения системной ошибки при неуспешном поиске"):
            browser.element('.catalog__search-results-message').\
                should(have.text(f'По запросу «{value}» ничего не найдено.'))

        """ ФИЛЬТРАЦИЯ """

    @staticmethod
    def filter_certificates():
        with allure.step('Клик по кнопке Искать'):
            browser.element('.search-form__submit').click()
        with allure.step('Выбрать toogle "Только с cертификатом"'):
            browser.element('[data-name="certificate"]').element('.ui-toggler').click()
        with allure.step('Проверка отображения лейбла "Только с cертификатом"'):
            browser.element('[data-type="certificate"]').should(be.visible)

    @staticmethod
    def filter_discount():
        with allure.step('Клик по кнопке Искать'):
            browser.element('.search-form__submit').click()
        with allure.step('Выбрать toogle "Только со скидкой"'):
            browser.element('[data-name="discount"]').element('.ui-toggler').click()
        with allure.step('Проверка отображения курса со скидкой'):
            browser.element('.display-price__price_discount').should(be.visible)

main_page = MainPage()