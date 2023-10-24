import os
import resource
from selene import browser, be, have, by, command


def test_form():
    browser.open('/automation-practice-form')
    # Name and Email
    browser.element('#firstName').should(be.blank).type('Test_name')
    browser.element('#lastName').should(be.blank).type('Test_Lastname')
    browser.element('#userEmail').should(be.blank).type('Test@test.com')
    # Choose gender +
    browser.element('[for=gender-radio-2]').click()
    # Write phone
    browser.element('#userNumber').should(be.blank).type('1234567890')
    # Calendar
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click().element(by.text('December')).click()
    browser.element('.react-datepicker__year-select').click().element(by.text('2020')).click()
    browser.element('.react-datepicker__day.react-datepicker__day--025').click()

    # Subject
    browser.element('#subjectsInput').type('Maths').press_enter()
    # Choose hobby
    # browser.element('[for=hobbies-checkbox-1]').click()
    browser.element('#hobbiesWrapper').perform(command.js.scroll_into_view).element(by.text('Sports')).click()
    # download file
    browser.element('#uploadPicture').send_keys(os.path.abspath('resourses/123.png'))
    # Write address
    browser.element('#currentAddress').type('Tbilisi')
    # Choose country and city
    browser.element('#state').click().element(by.text('NCR')).click()
    browser.element('#city').click().element(by.text('Delhi')).click()

    # Press button
    browser.element('#submit').press_enter()

    browser.element('.table').all('tr td:nth-child(2)').should(have.texts(
        'Test_name Test_Lastname',
        'Test@test.com',
        'Female',
        '1234567890',
        '25 December,2020',
        'Maths',
        'Sports',
        '123.png',
        'Tbilisi',
        'NCR Delhi'
    ))

    browser.element('#closeLargeModal').press_escape()  #кнопка перекрыта рекламой
