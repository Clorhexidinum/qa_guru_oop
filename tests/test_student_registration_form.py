import os
from selene.support.shared import browser
from selene import have, be


def test_submit_form():
    browser.open('/automation-practice-form')

    browser.element('#firstName').type('Murat')
    browser.element('#lastName').type('Kubekov')
    browser.element('#userEmail').type('test@gmail.com')

    browser.element('#gender-radio-1 + label').click()

    browser.element('#userNumber').type('89777777777')

    # Там где 2 варианта прошу дать комментарий как более правильно
    # browser.element('#dateOfBirthInput').should(be.blank).set_value("30 Oct 1991").press_enter()
    browser.element('.react-datepicker-wrapper').click()
    browser.element('.react-datepicker__month-select').type("October").press_enter()
    browser.element('.react-datepicker__year-select').type("1991").press_enter()
    browser.element('.react-datepicker__day[aria-label *= "October 30"]').click()
    # browser.all('.react-datepicker__day').filter_by(have.text('30'))[1].click()

    browser.element('#subjectsInput').type('Computer Science').press_enter().type('English').press_enter()

    browser.element('#hobbies-checkbox-1 + label').click()
    browser.element('#hobbies-checkbox-2 + label').click()
    browser.element('#hobbies-checkbox-3 + label').click()

    browser.element('#uploadPicture').send_keys(os.path.abspath('test_files/for_test_dont_remove.jpg'))

    browser.element('#currentAddress').type('Moskow, Ulitsa Pushkina, dom Kolotushkina')
    browser.element('#state').click()
    browser.element('#state input').type('NCR').press_enter()
    browser.element('#city').click()
    browser.element('#city input').type('Delhi').press_enter()

    browser.element('#submit').click()

    browser.element('.modal-content').should(be.visible)
    browser.all('.modal-body td+td').should(have.texts(
        'Murat Kubekov',
        'test@gmail.com',
        'Male',
        '8977777777',
        '30 October,1991',
        'Computer Science, English',
        'Sports, Reading, Music',
        'for_test_dont_remove.jpg',
        'Moskow, Ulitsa Pushkina, dom Kolotushkina',
        'NCR Delhi'))
