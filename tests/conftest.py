import pytest
from selene import browser, be, have
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

browser.element('#element_id').should(be.visible).click()


@pytest.fixture(scope='session')
def open_browser():
    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = 'eager'
    browser.config.driver_options = driver_options
    chrome_options = Options()
    chrome_options.add_argument('--headless')  # Запуск в безголовом режиме
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    browser.config.driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=chrome_options)
    browser.config.base_url = "https://github.com"
    browser.config.window_width = 1280
    browser.config.window_height = 720

    yield

    browser.quit()
