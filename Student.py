from types import SimpleNamespace
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import random
import string
import time
import json
from faker import Faker


allColleges = {
    'Mendocino College': {
        'url': 'https://www.opencccapply.net/gateway/apply?cccMisCode=141'
    },
    'Contra Costa College': {
        'url': 'https://www.opencccapply.net/gateway/apply?cccMisCode=311'
    },
    'Antelope Valley College': {
        'url': 'https://www.opencccapply.net/gateway/apply?cccMisCode=621'
    },
    'Southwestern College': {
        'url': 'https://www.opencccapply.net/gateway/apply?cccMisCode=091'
    },
    'Westmoreland College': {
        'url': 'https://apply.westmoreland.edu/Datatel.ERecruiting.Web.External/Pages/createaccount.aspx'
    },
    'Lansing College': {
        'url': 'https://starnetb.lcc.edu/LCCB/bwskalog.p_disploginnew?in_id=&cpbl=&newid='
    },
    'Durham Tech': {
        'url': 'https://auth.cfnc.org/Identity/Account/Register'
    }
}


class Student:

    email = ''
    college = ''
    firstName = ''
    middleName = ''
    lastName = ''
    streetAddress = ''
    cityAddress = ''
    stateAddress = ''
    postalCode = ''
    phone = ''
    ssn = ''
    username = ''
    password = ''
    pin = ''
    birthdayMonth = ''
    birthdayDay = ''
    birthdayYear = ''
    eduMonth = ''
    eduDay = ''
    eduYear = ''


def suffix(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return random.randint(range_start, range_end)


def build_student(driver, college):
    student = Student()
    fake = Faker()

    student.college = college
    first_name = fake.first_name_male()
    last_name = fake.last_name()

    print('Getting email', end='')

    driver.get('https://generator.email/email-generator')

    domain = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.ID, "email_ch_text"))
    ).text.split('@')[1]

    student.email = str.lower(first_name + last_name) + '@' + domain

    print(' (Complete)')

    student.firstName = first_name
    student.middleName = random.choice(string.ascii_uppercase)
    student.lastName = last_name

    get_new_address(student)

    student.phone = '202-555-' + str(suffix(4))

    student.ssn = fake.ssn().replace('-', '')

    student.username = student.firstName[:3] + str(suffix(5))
    student.password = student.lastName + str(suffix(5))
    if college == 'Lansing College':
        student.pin = str(suffix(8))
    elif college == 'Stockton University':
        student.pin = first_name[0] + str(suffix(7))
    else:
        student.pin = str(suffix(4))

    student.birthdayMonth = str(random.randint(1, 12))
    student.birthdayDay = str(random.randint(1, 27))
    student.birthdayYear = str(random.randint(1996, 1999))
    student.eduMonth = str(random.randint(1, 12))
    student.eduDay = str(random.randint(1, 27))
    student.eduYear = str(random.randint(2019, 2020))

    return student


def get_new_address(student):
    with open('addresses.json', 'r') as f:
        addresses = json.load(f, object_hook=lambda d: SimpleNamespace(**d))

    while True:
        address = random.choice(addresses.addresses)
        if address.address2 == '':
            student.streetAddress = address.address1
            student.cityAddress = address.city
            student.stateAddress = address.state
            student.postalCode = address.postalCode
            break
        else:
            continue


def save_student(student):
    with open('students.txt', 'a') as f:
        f.write(json.dumps(vars(student)) + '\n')


def get_student_from_file():
    student_list = []
    index = 1
    with open('students.txt', 'r') as f:
        lines = f.readlines()

    for line in lines:
        student = json.loads(line, object_hook=lambda d: SimpleNamespace(**d))
        if student.college == 'Westmoreland College':
            student.index = index
            student_list.append(student)
            index += 1

    print('\nSelect a student:')
    for student in student_list:
        print(str(student.index) + ' - ' + student.email)

    while True:
        data = int(input())
        if data > len(student_list) or data < 1:
            print("Invalid response, try again.")
            continue
        else:
            break

    for student in student_list:
        if student.index == data:
            return student

    return None
