from selene import have, command
from selene.support.shared import browser
from demoqa_tests.model.controls.radio import Radio
from demoqa_tests.model.controls.datepicker import DatePicker
from demoqa_tests.model.controls.checkbox import Checkbox
from demoqa_tests.model.controls.dropdown import DropDown
from demoqa_tests.model.data import users
from demoqa_tests.utils import path


class RegistrationForm:
    def __init__(self):
        self.gender = Radio('gender-radio')
        self.birthday = DatePicker(browser.element('#dateOfBirthInput'))
        self.hobby_checkbox = Checkbox('hobbies-checkbox')
        self.state_dropdown = DropDown(browser.element('#state'))
        self.city_dropdown = DropDown(browser.element('#city'))

    def given_opened(self):
        browser.open('/automation-practice-form')
        ads = browser.elements('[id^=google_ads][id$=container__]')
        if ads.with_(timeout=10).wait.until(have.size_greater_than_or_equal(3)):
            ads.perform(command.js.remove)
        return self

    def set_firstname(self, firstname: str):
        browser.element('#firstName').type(firstname)
        return self

    def set_lastname(self, firstname: str):
        browser.element('#lastName').type(firstname)
        return self

    def set_email(self, email: str):
        browser.element('#userEmail').type(email)
        return self

    def set_gender(self, gender: users.Gender):
        self.gender.select(gender)
        return self

    def set_phone(self, phone: str):
        browser.element('#userNumber').type(phone)
        return self

    def set_date_of_birth(self, day, month, year):
        self.birthday.type_date(day, month, year)
        return self

    def set_subjects(self, values: users.Subject):
        for subject in values:
            browser.element('#subjectsInput').type(subject.value).press_enter()
        return self

    def set_hobbies(self, hobbies: users.Hobby):
        for hobby in hobbies:
            self.hobby_checkbox.select('hobbies-checkbox', hobby.value)
        return self

    # я хз почему не работает, пишет AttributeError: 'tuple' object has no attribute 'value'
    # def set_hobbies(*options: users.Hobby):
    #     checkbox.select(*[option.value for option in options])
    #     # for hobby in hobbies:
    #     #     checkbox.select('hobbies-checkbox', hobby.value)

    def select_picture(self, file):
        browser.element('#uploadPicture').send_keys(path.to_resource(file))
        return self

    def set_adress(self, adress: str):
        browser.element('#currentAddress').type(adress)
        return self

    def set_state(self, value: str):
        self.state_dropdown.select(value)
        return self

    def set_city(self, value: str):
        self.city_dropdown.select(value)
        return self

    def scroll_to_bottom(self):
        browser.element('#state').perform(command.js.scroll_into_view)
        return self

    def submit(self):
        browser.element('#submit').perform(command.js.click)
        return self
