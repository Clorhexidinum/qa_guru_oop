from selene import have
from selene.support.shared import browser


def select(element_id, value):
    browser.all(f'[id^={element_id}]').element_by(have.value(value)).element('..').click()
