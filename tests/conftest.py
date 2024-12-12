import pytest
from selene import browser


@pytest.fixture(scope='session')
def open_browser():
    browser.config.base_url = "https://github.com"