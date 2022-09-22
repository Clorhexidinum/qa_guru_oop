from selene import have, command, by
from selene.support.shared import browser

from demoqa_tests.model import app
from demoqa_tests.model.pages import registration_form
from demoqa_tests.utils import path
from tests.test_data.users import murat

def test_submit_student_registration_form():

    registration_form.given_opened()

    # WHEN

    browser.element('#firstName').type(murat.first_name)
    browser.element('#lastName').type(murat.last_name)
    browser.element('#userEmail').type(murat.email)

    '''
    browser.all('[for^=gender-radio]').by(
        have.exact_text(murat.gender.value)
    ).first.click()
    
    # OR
    gender_male = browser.element('[for=gender-radio-1]')
    gender_male.click()
    # OR
    browser.element('[id^=gender-radio][value=Male]').perform(command.js.click)
    browser.element('[id^=gender-radio][value=Male]').element(
        './following-sibling::*'
    ).click()
    # OR better:
    browser.element('[id^=gender-radio][value=Male]').element('..').click()
    # OR
    browser.all('[id^=gender-radio]').element_by(have.value('Male')).element('..').click()
    browser.all('[id^=gender-radio]').by(have.value('Male')).first.element('..').click()
    '''
    browser.element('#userNumber').type(murat.user_number)

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').send_keys(murat.birth_month)
    browser.element('.react-datepicker__year-select').send_keys(murat.birth_year)
    browser.element(
        f'.react-datepicker__day--0{murat.birth_day}'
        f':not(.react-datepicker__day--outside-month)'
    ).click()
    '''
    # OR something like
    browser.element('#dateOfBirthInput').send_keys(Keys.CONTROL, 'a').type('28 Mar 1995').press_enter()
    '''

    registration_form.add_subjects(murat.subjects)

    for hobby in murat.hobbies:
        # browser.element(f'//label[contains(.,"{hobby.value}")]').click()
        # browser.element(by.text(hobby.value, tag='label')).click()
        browser.all('[id^=hobbies]').by(have.value(hobby.value)).first.element(
            '..'
        ).click()

    browser.element('[id="uploadPicture"]').send_keys(
        path.to_resource(murat.picture_file)
    )

    browser.element('#currentAddress').type(murat.current_address)

    registration_form.scroll_to_bottom()

    registration_form.set_state(murat.state)
    registration_form.set_city(murat.city)

    browser.element('#submit').perform(command.js.click)

    # THEN

    registration_form.should_have_submitted(
        [
            ('Student Name', f'{murat.name} {murat.last_name}'),
            ('Student Email', murat.email),
            ('Gender', murat.gender.value),
        ],
    )