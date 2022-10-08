from selene import have
from selene.support.shared import browser


class Checkbox:
    def __init__(self, elements):
        self.elements = elements

    def select(self, element_selector: str, text: str):
        browser.all(f'[for^={element_selector}]').by(have.text(text)).first.element('..').click()

# я хз почему не работает, пишет AttributeError: 'tuple' object has no attribute 'value'
#     def select(self, element_selector: str, *options: str):
#         for option in options:
#             browser.all(f'[for^={element_selector}]').by(have.text(option)).first.element('..').click()
