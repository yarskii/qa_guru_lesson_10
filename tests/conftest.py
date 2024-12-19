import pytest
from selene import browser, be
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='session')
def open_browser():
    chrome_options = Options()
    chrome_options.add_argument('--headless')  # Запуск в безголовом режиме
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')

    driver_service = Service(ChromeDriverManager().install())
    browser.config.driver = webdriver.Chrome(service=driver_service, options=chrome_options)

    browser.config.base_url = "https://github.com"
    browser.config.window_width = 1280
    browser.config.window_height = 720

    yield

    browser.quit()
