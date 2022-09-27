from demoqa_tests.model.pages import registration_form
from tests.test_data.users import murat
from demoqa_tests.utils import turpl_to_string


def test_submit_form():
    # GIVEN
    registration_form.given_opened()

    # WHEN
    registration_form.set_firstname(murat.first_name)
    registration_form.set_lastname(murat.last_name)
    registration_form.set_email(murat.email)
    registration_form.set_gender(murat.gender.value)
    registration_form.set_phone(murat.phone_number)
    registration_form.type_date_of_birth(murat.birth_day, murat.birth_month, murat.birth_year)
    registration_form.add_subjects(murat.subjects)
    registration_form.set_hobbies(murat.hobbies)
    registration_form.upload_file(murat.picture_file)
    registration_form.set_adress(murat.current_address)
    registration_form.scroll_to_bottom()
    registration_form.set_state(murat.state)
    registration_form.set_city(murat.city)
    registration_form.submit()

    # THEN
    registration_form.assert_form_sent()
    registration_form.should_have_submitted(
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

