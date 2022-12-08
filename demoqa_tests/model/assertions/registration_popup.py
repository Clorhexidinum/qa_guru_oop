from selene.support.conditions import be, have
from selene.support.shared import browser

from demoqa_tests.model.components import modal


def should_visible():
    browser.element('.modal-body').should(be.visible)


def should_have_submitted(data):
    rows = modal.dialog.all('tbody tr')
    for row, value in data:
        rows.element_by(have.text(row)).all('td')[1].should(have.exact_text(value))