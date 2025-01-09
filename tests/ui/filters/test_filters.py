import allure
from page.main_page import main_page


@allure.label("owner", "aa.eliseev")
@allure.feature('Фильтрация')
@allure.title('Фильтрация курсов "Только с сертификатом"')
@allure.severity(allure.severity_level.CRITICAL)
@allure.epic('UI')
@allure.tag("Smoke")
def test_filters_with_certificates(setup_browser):
    main_page.open_page()
    main_page.filter_certificates()


@allure.label("owner", "aa.eliseev")
@allure.feature('Фильтрация')
@allure.title('Фильтрация курсов "Только со скидкой"')
@allure.severity(allure.severity_level.CRITICAL)
@allure.epic('UI')
@allure.tag("Smoke")
def test_filters_with_certificates(setup_browser):
    main_page.open_page()
    main_page.filter_discount()