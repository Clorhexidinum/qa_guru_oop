from selene import have
from selene.support.shared import browser


def select(value):
    browser.all('[id^=gender-radio]').element_by(have.value(value)).element('..').click()
