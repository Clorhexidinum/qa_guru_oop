import platform
from selene import Element, command
from selene.support.conditions import have
from selene.support.shared import browser
from selenium.webdriver import Keys


class DatePicker:
    def __init__(self, element: Element):
        self.element = element

    def select_date(self, year, month, day):
        self.element.click()
        browser.element('.react-datepicker__month-select').send_keys(month)
        browser.element('.react-datepicker__year-select').send_keys(year)
        browser.element(
            f'.react-datepicker__day--0{day}'
            f':not(.react-datepicker__day--outside-month)'
        ).click()

    def type_date(self, day, month, year):
        format_str = f'{day} {month},{year}'
        os_base = platform.system()
        if os_base == 'Darwin':
            self.element.send_keys(Keys.COMMAND + 'a').type(format_str).press_enter()
        else:
            self.element.send_keys(Keys.CONTROL + 'a').type(format_str).press_enter()

    def select_month(self, month):
        browser.element('.react-datepicker__month-select').click()
        browser.all('.react-datepicker__month-select option').element_by(have.text(month)).first.press_enter()

    def select_year(self, year):
        browser.element('.react-datepicker__year-select').click()
        element_year = browser.all('.react-datepicker__year-select option').element_by(have.text(year)).first
        element_year.perform(command.js.scroll_into_view)
        element_year.press_enter()

    def select_day(self, day):
        browser.element(
            f'.react-datepicker__day--0{day}'
            f':not(.react-datepicker__day--outside-month)'
        ).press_enter()
