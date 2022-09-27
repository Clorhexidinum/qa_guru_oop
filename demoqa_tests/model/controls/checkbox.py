from selene import have
from selene.support.shared import browser


def select(hobby):
    # browser.all('[id^=hobbies-checkbox]').element_by(have.value(hobby)).element('..').click()
    browser.all('[for^=hobbies-checkbox]').element_by(have.text(hobby)).element('..').click()