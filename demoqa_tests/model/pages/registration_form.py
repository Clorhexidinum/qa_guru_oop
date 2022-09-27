import os
import platform
from typing import Tuple
from selene import have, command
from selene.support.conditions import be
from selene.support.shared import browser
from demoqa_tests.model.controls import dropdown, modal, radio, datepicker, checkbox
from tests.test_data.users import Subject
from selenium.webdriver.common.keys import Keys
from demoqa_tests.utils import path

state = browser.element('#state')


def given_opened():
    browser.open('/automation-practice-form')
    ads = browser.elements('[id^=google_ads][id$=container__]')
    if ads.with_(timeout=10).wait.until(have.size_greater_than_or_equal(3)):
        ads.perform(command.js.remove)


def set_firstname(firstname: str):
    browser.element('#firstName').type(firstname)


def set_lastname(firstname: str):
    browser.element('#lastName').type(firstname)


def set_email(email: str):
    browser.element('#userEmail').type(email)


def set_gender(gender):
    radio.select(gender)


def set_phone(phone: str):
    browser.element('#userNumber').type(phone)


def set_date_of_birth(date: list):
    browser.element('#dateOfBirthInput').click()
    datepicker.select_month(date[1])
    datepicker.select_year(date[2])
    datepicker.select_day(date[1], date[0])


def type_date_of_birth(day, month, year):
    format_str = f'{day} {month},{year}'
    os_base = platform.system()
    if os_base == 'Darwin':
        browser.element('#dateOfBirthInput').send_keys(Keys.COMMAND + 'a').type(format_str).press_enter()
    else:
        browser.element('#dateOfBirthInput').send_keys(Keys.CONTROL + 'a').type(format_str).press_enter()


def add_subjects(values: Tuple[Subject]):
    for subject in values:
        browser.element('#subjectsInput').type(subject.value).press_enter().press_escape()


def set_hobbies(hobbies: Tuple[Subject]):
    for hobby in hobbies:
        checkbox.select(hobby.value)


def upload_file(file):
    browser.element('#uploadPicture').send_keys(path.to_resource(file))

def set_adress(adress: str):
    browser.element('#currentAddress').type(adress)


def set_state(value: str):
    dropdown.select(state, value)


def set_city(value: str):
    dropdown.select(browser.element('#city'), value)


def scroll_to_bottom():
    state.perform(command.js.scroll_into_view)


def submit():
    browser.element('#submit').perform(command.js.click)


def assert_form_sent():
    browser.element('.modal-body').should(be.visible)


def should_have_submitted(data):
    rows = modal.dialog.all('tbody tr')
    for row, value in data:
        rows.element_by(have.text(row)).all('td')[1].should(have.exact_text(value))
