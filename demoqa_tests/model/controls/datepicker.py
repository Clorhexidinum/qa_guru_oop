from selene import command
from selene.support.conditions import have
from selene.support.shared import browser


def select_month(month):
    browser.element('.react-datepicker__month-select').click()
    browser.all('.react-datepicker__month-select option').element_by(have.text(month)).first.press_enter()


def select_year(year):
    browser.element('.react-datepicker__year-select').click()
    element_year = browser.all('.react-datepicker__year-select option').element_by(have.text(year)).first
    element_year.perform(command.js.scroll_into_view)
    element_year.press_enter()


def select_day(day):
    browser.element(
        f'.react-datepicker__day--0{day}'
        f':not(.react-datepicker__day--outside-month)'
    ).press_enter()
