from selene import browser, be, by, command, have
import resources


class RegistrationPage:
    def __init__(self):
        self.file = browser.element('#uploadPicture')

    def open(self):
        browser.open('/automation-practice-form')
        return self

    def fill_first_name(self, name):
        browser.element('#firstName').should(be.blank).type(name)
        return self

    def fill_last_name(self, last_name):
        browser.element('#lastName').type(last_name)
        return self

    def email(self, email):
        browser.element('#userEmail').type(email)
        return self

    def gender(self):
        browser.element('[for=gender-radio-2]').click()
        return self

    def phone(self, number):
        browser.element('#userNumber').should(be.blank).type(number)
        return self

    def birthdate(self, day, month, year):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').click().element(by.text(month)).click()
        browser.element('.react-datepicker__year-select').click().element(by.text(year)).click()
        browser.element(f'.react-datepicker__day.react-datepicker__day--0{day}').click()
        return self

    def fill_subject(self, subject_name):
        browser.element('#subjectsInput').type(subject_name).press_enter()
        return self

    def fill_hobbies(self, type):
        browser.element('#hobbiesWrapper').perform(command.js.scroll_into_view).element(by.text(type)).click()
        return self

    def download_file(self, file):
        # self.file.send_keys(os.path.abspath(f'resources/{file}'))
        self.file.send_keys(resources.path(file))
        return self

    def fill_address(self, value):
        browser.element('#currentAddress').type(value)
        return self

    def state_and_city(self, state, city):
        browser.element('#state').click().element(by.text(state)).click()
        browser.element('#city').click().element(by.text(city)).click()
        return self

    def submit(self):
        browser.element('#submit').press_enter()
        return self

    def should_registered_user_with(self, name, email, gender, phone, birthdate, subject, hobby, file, address,
                                    state_city):
        browser.element('.table').all('tr td:nth-child(2)').should(have.texts(
            name,
            email,
            gender,
            phone,
            birthdate,
            subject,
            hobby,
            file,
            address,
            state_city
        ))
        return self

    def remove_ads(self):
        browser.all('[id^=google_ads][id$=container__]').with_(timeout=10).wait_until(
            have.size_greater_than_or_equal(3))
        browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)
        return self

