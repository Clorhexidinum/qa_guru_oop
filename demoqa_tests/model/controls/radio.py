from selene import have
from selene.support.shared import browser


def select(gender):
    browser.all('[id^=gender-radio]').element_by(have.value(gender)).element('..').click()
