import allure
from allure_commons.types import Severity
from demoqa_tests.model.pages import registration_form
from demoqa_tests.model.assertions import registration_popup
from demoqa_tests.model.data.users import murat
from demoqa_tests.utils import turpl_to_string, attach
from selene.support.shared import browser


@allure.tag("web")
@allure.severity(Severity.MINOR)
@allure.label("owner", "Murat")
@allure.feature("Задачи в DemoQA")
@allure.story("Пользователь может отправить валидно заполненную форму")
@allure.link("https://demoqa.com/automation-practice-form", name="Demo QA")
def test_submit_form():
    with allure.step("Открываем главную страницу"):
        registration_form.given_opened()
    with allure.step('В поле First Name вводим значение "user.first_name"'):
        registration_form.set_firstname(murat.first_name)
    with allure.step('В поле Last Name вводим значение "user.last_name"'):
        registration_form.set_lastname(murat.last_name)
    with allure.step('В поле Email вводим значение "user.email"'):
        registration_form.set_email(murat.email)
    with allure.step('В поле Gender выбираем значение "user.gender.value"'):
        registration_form.set_gender(murat.gender.value)
    with allure.step('В поле Mobile вводим значение "user.phone_number"'):
        registration_form.set_phone(murat.phone_number)
    with allure.step('В поле Date of Birth вводим значения "user.birth_day, user.birth_month, user.birth_year"'):
        registration_form.set_date_of_birth(murat.birth_day, murat.birth_month, murat.birth_year)
    with allure.step('В поле Subjects вводим значения "user.subjects"'):
        registration_form.set_subjects(murat.subjects)
    with allure.step('В поле Hobbies выбираем значения "user.subjects"'):
        registration_form.set_hobbies(murat.hobbies)
    with allure.step('В поле Picture загружаем файл "user.picture_file"'):
        registration_form.select_picture(murat.picture_file)
    with allure.step('В поле Current Address выбираем значения "user.current_address"'):
        registration_form.set_adress(murat.current_address)
    registration_form.scroll_to_bottom()
    with allure.step('В поле Select state выбираем значения "user.state"'):
        registration_form.set_state(murat.state)
    with allure.step('В поле Select city выбираем значения "user.state"'):
        registration_form.set_city(murat.city)
    with allure.step("Отправляем форму"):
        registration_form.submit()
    with allure.step("Проверяем что появился попап"):
        registration_popup.should_visible()

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    with allure.step("Проверяем данные в попапе"):
        registration_popup.should_have_submitted(
            [
                ('Student Name', f'{murat.first_name} {murat.last_name}'),
                ('Student Email', murat.email),
                ('Gender', murat.gender.value),
                ('Mobile', '8977777777'),
                ('Date of Birth', f'{murat.birth_day} {murat.birth_month},{murat.birth_year}'),
                ('Subjects', turpl_to_string.convert(murat.subjects)),
                ('Hobbies', turpl_to_string.convert(murat.hobbies)),
                ('Picture', murat.picture_file),
                ('Address', murat.current_address),
                ('State and City', f'{murat.state} {murat.city}')
            ],
        )
