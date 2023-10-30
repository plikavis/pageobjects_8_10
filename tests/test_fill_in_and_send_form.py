import os
import resource
from selene import browser, be, have, by, command

from pageobjects_8_10.data.users import User
from pageobjects_8_10.model.regitration_page import RegistrationPage


def test_form():
    admin = User(name='Test_name',
                 lastName='Test_Lastname',
                 email='Test@test.com',
                 gender='Female',
                 phone='1234567890',
                 day='25',
                 month='December',
                 year='2020',
                 subject='Maths',
                 hobby='Sports',
                 file='123.png',
                 address='Tbilisi',
                 state='NCR',
                 city='Delhi'
                 )
    registration_page = RegistrationPage()
    registration_page.open()
    registration_page.register(admin)
    registration_page.should_have_registered(admin)
    registration_page.exit()  # кнопка перекрыта рекламой
