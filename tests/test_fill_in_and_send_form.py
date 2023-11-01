from selene import browser, have, command
from pageobjects_8_10.registration_page import RegistrationPage


def test_form():
    registration_page = RegistrationPage()
    registration_page.open()
    registration_page.remove_ads()
    # Name and Email
    registration_page.fill_first_name('Test_name')
    registration_page.fill_last_name('Test_Lastname')
    registration_page.email('Test@test.com')  # browser.element('#userEmail').should(be.blank).type('Test@test.com')
    # Choose gender
    registration_page.gender()  # browser.element('[for=gender-radio-2]').click()
    # Write phone
    registration_page.phone('1234567890')  # browser.element('#userNumber').should(be.blank).type('1234567890')
    # Calendar
    registration_page.birthdate('25', 'December', '2020')
    # Subject
    registration_page.fill_subject('Maths')
    # Choose hobby
    registration_page.fill_hobbies('Sports')
    # download file
    registration_page.download_file('123.png')
    # Write address
    registration_page.fill_address('Tbilisi')
    # Choose country and city
    registration_page.state_and_city('NCR', 'Delhi')
    # Press button
    registration_page.submit()
    registration_page.should_registered_user_with('Test_name Test_Lastname',
                                                  'Test@test.com',
                                                  'Female',
                                                  '1234567890',
                                                  '25 December,2020',
                                                  'Maths',
                                                  'Sports',
                                                  '123.png',
                                                  'Tbilisi',
                                                  'NCR Delhi')

    browser.element('#closeLargeModal').press_escape()  # кнопка перекрыта рекламой
