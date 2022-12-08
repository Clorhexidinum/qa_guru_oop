from selene.support.shared import browser


def given_opened_browser(url):
    browser.open(url)
    browser.driver.maximize_window()