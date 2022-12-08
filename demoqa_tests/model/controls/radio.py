from selene import have
from selene.support.shared import browser


class Radio:
    def __init__(self, element_id: str):
        self.element = element_id

    def select(self, value):
        browser.all(f'[id^={self.element}]').element_by(have.value(value)).element('..').click()

