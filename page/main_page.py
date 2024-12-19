import allure
from selene import browser, have


class MainPage:

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

    def open_page(self):
        with allure.step("Открыть браузер"):
            browser.open('/')
            return self

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


main_page = MainPage()