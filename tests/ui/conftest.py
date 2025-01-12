import os
import pytest
from selene import browser


@pytest.fixture(scope='function', autouse=True)
def browser_settings():
    browser.config.timeout = 12
    browser.config.window_height = 1080
    browser.config.window_width = 1920
    browser.config.base_url = os.getenv('URL')
