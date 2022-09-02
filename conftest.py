import pytest
from selene.support.shared import browser, config
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def get_chrome_options():
    options = Options()
    # options.add_argument('chrome')  # Use headless if you do not need a browser UI
    # options.add_argument('--start-maximized')
    # options.add_argument('--window-size=1920,1080')
    # options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.page_load_strategy = 'eager'
    return options


@pytest.fixture()
def get_webdriver(get_chrome_options):
    browser.config.driver = webdriver.Chrome(options=get_chrome_options)
    return browser.config.driver

@pytest.fixture()
def open_browser(request, get_webdriver):
    browser.open('https://staging-ru.maximumtest.test01.maximumtest.ru/ege')
    yield
    browser.close_current_tab()
