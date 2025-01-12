import allure
from framework_ui.page.main_page import main_page


@allure.label("owner", "aa.eliseev")
@allure.feature('Фильтрация')
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("Smoke")
@allure.title('Фильтрация курсов "Только с сертификатом"')
@allure.story('UI')
def test_filters_with_certificates(setup_browser):
    main_page.open_page()
    main_page.filter_certificates()


@allure.label("owner", "aa.eliseev")
@allure.feature('Фильтрация')
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("Smoke")
@allure.title('Фильтрация курсов "Только со скидкой"')
@allure.story('UI')
def test_filters_with_discount(setup_browser):
    main_page.open_page()
    main_page.filter_discount()