import allure
import pytest

from page.main_page import main_page


@allure.label("owner", "aa.eliseev")
@allure.feature('Поиск')
@allure.tag("Smoke")
@pytest.mark.parametrize('value',
                         [item[0] for item in main_page.get_search_item_success()],
                         ids=[item[1] for item in main_page.get_search_item_success()]
                         )
def test_search_success(setup_browser, value):
    allure.dynamic.title(f'Проверка успешного поиска на сайте при вводе: {value}')
    main_page.open_page()
    main_page.search_success(value)


@allure.label("owner", "aa.eliseev")
@allure.feature('Поиск')
@allure.tag("Smoke")
@pytest.mark.parametrize('value',
                         [item[0] for item in main_page.get_search_item_failure()],
                         ids=[item[1] for item in main_page.get_search_item_failure()]
                         )
def test_search_failure(setup_browser, value):
    allure.dynamic.title(f'Проверка неудачного поиска на сайте при вводе: {value}')
    main_page.open_page()
    main_page.search_failure(value)
