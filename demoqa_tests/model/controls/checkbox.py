from selene import have
from selene.support.shared import browser


def select(text):
    browser.all('[for^=hobbies-checkbox]').element_by(have.text(text)).element('..').click()