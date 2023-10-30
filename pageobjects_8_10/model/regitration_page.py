import os
from selene import browser, by, command, have
from pageobjects_8_10.data.users import User


class RegistrationPage:
    def __init__(self):
        self.city = browser.element('#city')
        self.state = browser.element('#state')
        self.close = browser.element('#closeLargeModal')
        self.file = browser.element('#uploadPicture')
        self.hobby = browser.element('#hobbiesWrapper')
        self.subject = browser.element('#subjectsInput')
        self.phone = browser.element('#userNumber')
        self.first_name = browser.element('#firstName')
        self.last_name = browser.element('#lastName')
        self.gender = browser.element('[for=gender-radio-2]')
        self.email = browser.element('#userEmail')
        self.address = browser.element('#currentAddress')
        self.number = browser.element('##userNumber')
        self.submit_button = browser.element('#submit')

    def open(self):
        browser.open('/automation-practice-form')
        return self

    def fill_full_name(self, name, lastname):
        self.first_name.type(name)
        self.last_name.type(lastname)
        return self

    def fill_email(self, email):
        self.email.type(email)
        return self

    def fill_gender(self):
        self.gender.click()
        return self

    def fill_phone(self, value):
        self.phone.type(value)
        return self

    def fill_date_of_birth(self, day, month, year):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').click().element(by.text(month)).click()
        browser.element('.react-datepicker__year-select').click().element(by.text(year)).click()
        browser.element(f'.react-datepicker__day.react-datepicker__day--0{day}').click()
        return self

    def fill_subject(self, value):
        self.subject.type(value).press_enter()
        return self

    def fill_hobby(self, value):
        self.hobby.perform(command.js.scroll_into_view).element(by.text(value)).click()
        return self

    def download_file(self, name):
        self.file.send_keys(os.path.abspath(f'resourses/{name}'))
        return self

    def fill_address(self, value):
        self.address.type(value)
        return self

    def fill_state_city(self, state, city):
        self.state.click().element(by.text(state)).click()
        self.city.click().element(by.text(city)).click()
        return self

    def submit(self):
        browser.element('#submit').press_enter()
        return self

    def register(self, user: User):
        self.fill_full_name(user.name, user.lastName)
        self.fill_email(user.email)
        self.fill_gender()
        self.fill_phone(user.phone)
        self.fill_date_of_birth(user.day, user.month, user.year)
        self.fill_subject(user.subject)
        self.fill_hobby(user.hobby)
        self.download_file(user.file)
        self.fill_address(user.address)
        self.fill_state_city(user.state, user.city)
        self.submit()

    def should_have_registered(self, user: User):
        browser.element('.table').all('tr td:nth-child(2)').should(have.texts(
            'Test_name Test_Lastname',
            user.email,
            user.gender,
            user.phone,
            f'{user.day} {user.month},{user.year}',
            user.subject,
            user.hobby,
            user.file,
            user.address,
            f'{user.state} {user.city}'
        ))
        return self

    def exit(self):
        self.close.press_escape()

