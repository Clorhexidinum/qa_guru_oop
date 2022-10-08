import allure
from allure_commons.types import Severity
from demoqa_tests.model.pages.registration_form import RegistrationForm
from demoqa_tests.model.assertions import registration_popup
from demoqa_tests.model.data.users import murat
from demoqa_tests.utils import turpl_to_string


@allure.tag("web")
@allure.severity(Severity.MINOR)
@allure.label("owner", "Murat")
@allure.feature("Задачи в DemoQA")
@allure.story("Пользователь может отправить валидно заполненную форму")
@allure.link("https://demoqa.com/automation-practice-form", name="Demo QA")
def test_submit_form():
    registration = RegistrationForm()
    with allure.step("Открываем главную страницу"):
        registration.given_opened()
    with allure.step("Заполняем форму"):
        (registration
         .set_firstname(murat.first_name)
         .set_lastname(murat.last_name)
         .set_email(murat.email)
         .set_gender(murat.gender.value)
         .set_phone(murat.phone_number)
         .set_date_of_birth(murat.birth_day, murat.birth_month, murat.birth_year)
         .set_subjects(murat.subjects)
         .set_hobbies(murat.hobbies)
         .select_picture(murat.picture_file)
         .set_adress(murat.current_address)
         .scroll_to_bottom()
         .set_state(murat.state)
         .set_city(murat.city)
         )
    with allure.step("Отправляем форму"):
        registration.submit()

    with allure.step("Проверяем что появился попап"):
        registration_popup.should_visible()

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
