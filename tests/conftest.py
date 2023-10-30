import pytest
from selene import browser


@pytest.fixture(scope='function', autouse=True)
def browser_settings():
    browser.config.window_height = 1000
    browser.config.window_width = 600
    browser.config.base_url = 'https://demoqa.com'

    yield

    browser.quit()