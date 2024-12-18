from selene import browser
import os
from dotenv import load_dotenv
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from utils import attach

DEFAULT_BROWSER_VERSION = '125.0'
DEFAULT_SELENOID_URL = 'selenoid.autotests.cloud/wd/hub'

def pytest_addoption(parser):

    parser.addoption(
        '--browser_version',
        default=DEFAULT_BROWSER_VERSION
    )

    parser.addoption(
        '--run_mode',
        help=' Режим запуска тестов (local or remote)',
        choices=['remote', 'local'],
        default='local'
    )

    parser.addoption(
        '--selenoid_url',
        default=DEFAULT_SELENOID_URL
    )

    parser.addoption(
        '--browser',
        help=' Режим выбора браузера',
        choices=['chrome', 'firefox'],
        default='chrome'
    )


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope="session", autouse=True)
def setup_browser(request):
    browser_version = request.config.getoption('--browser_version')
    run_mode = request.config.getoption('--run_mode')
    selected_browser = request.config.getoption('--browser')
    driver = None

    if run_mode == 'remote':
        selenoid_capabilities = {
            "browserName": selected_browser,
            "browserVersion": browser_version,
            "selenoid:options": {
                "enableVNC": True,
                "enableVideo": True
            }
        }

        options = ChromeOptions() if selected_browser == 'chrome' else FirefoxOptions()
        options.capabilities.update(selenoid_capabilities)

        if selected_browser == 'chrome':
            options.page_load_strategy = 'eager'
        elif selected_browser == 'firefox':
            options.page_load_strategy = 'eager'

        selenoid_login = os.getenv('SELENOID_LOGIN')
        selenoid_password = os.getenv('SELENOID_PASSWORD')
        selenoid_url = request.config.getoption('--selenoid_url')
        selenoid_url = selenoid_url if selenoid_url != '' else os.getenv('SELENOID_URL')

        driver = webdriver.Remote(
            command_executor=f"https://{selenoid_login}:{selenoid_password}@{selenoid_url}",
            options=options)

    else:
        if selected_browser == 'chrome':
            options = ChromeOptions()
            options.page_load_strategy = 'eager'
            driver = webdriver.Chrome(options=options)
        elif selected_browser == 'firefox':
            options = FirefoxOptions()
            options.page_load_strategy = 'eager'
            driver = webdriver.Firefox(options=options)

    browser.config.driver = driver
    browser.config.window_height = 1080
    browser.config.window_width = 1920
    browser.config.base_url = os.getenv('URL')

    yield

    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    if run_mode == 'remote':
        attach.add_video(browser)

    browser.quit()