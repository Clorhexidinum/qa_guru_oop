import pytest
from selene.support.shared import browser


@pytest.fixture()
def open_browser():
    browser.open('https://google.com')
    yield
    browser.close()
