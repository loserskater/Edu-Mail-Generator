from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import random
import time
import Student

# 'MOTT College': {
#         'url': 'https://appsprod.mcc.edu/onlineapp'
#     }


def apply(driver, student):
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "gender"))
    )

    Select(driver.find_element_by_id('gender')).select_by_value('M')

    Select(driver.find_element_by_id('title')).select_by_value('Mr.')

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "first_name"))
    ).send_keys(student.firstName)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "last_name"))
    ).send_keys(student.lastName)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "address"))
    ).click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "address"))
    ).send_keys(student.streetAddress)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "zip"))
    ).click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "zip"))
    ).send_keys(student.postalCode)

    Select(driver.find_element_by_id('state')).select_by_value(student.stateAddress)
    Select(driver.find_element_by_id('phonetype')).select_by_value('CELL')

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "phone"))
    ).click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "phone"))
    ).send_keys(student.phone)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "email"))
    ).send_keys(student.email)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "confirm_email"))
    ).send_keys(student.email)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[contains(text(),'Next')]"))
    ).click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "uscitizenyes"))
    ).click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "ssnyes"))
    ).click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "ssn"))
    ).send_keys(student.ssn)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "confirm_ssn"))
    ).send_keys(student.ssn)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "dateofbirth"))
    ).send_keys(student.birthdayMonth + student.birthdayDay + student.birthdayYear)

    Select(driver.find_element_by_id('countryofbirth')).select_by_value('USA')

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[contains(text(),'Next')]"))
    ).click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "hsgradstatus"))
    )

    Select(driver.find_element_by_id('hsgradstatus')).select_by_value('Y')
    Select(driver.find_element_by_id('hsgradyear')).select_by_value(student.eduYear)

    options = Select(driver.find_element_by_id('hsattend')).options
    Select(driver.find_element_by_id('hsattend')).select_by_index(random.randint(1, len(options)))
    Select(driver.find_element_by_id('studenttype')).select_by_value('FTF')
    Select(driver.find_element_by_id('studentstatus')).select_by_value('F')
    Select(driver.find_element_by_id('studentsemester')).select_by_value('F21/22')
    Select(driver.find_element_by_id('studentgoal')).select_by_value('TRM')
    Select(driver.find_element_by_id('campuspreference')).select_by_index(random.randint(1, 5))

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "selectMajorButton"))
    ).click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[contains(text(),'Transferable Associate Degrees')]"))
    ).click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[contains(text(),'Associate in Science')]"))
    ).click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[contains(text(),'Next')]"))
    ).click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "howdidyou"))
    )

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[contains(text(),'Next')]"))
    ).click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "hispaniclatinoNo"))
    )

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[contains(text(),'Next')]"))
    ).click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "studentlifeynn"))
    ).click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[contains(text(),'Next')]"))
    ).click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "verify"))
    ).click()

    print('Please fill the captcha and click Review and then Submit')

    wait = 180
    while True:
        mins, secs = divmod(wait, 60)
        timeformat = '\rWaiting {:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='')
        try:
            driver.find_element_by_xpath("//*[contains(text(),'Thank you')]")
            print('\rCaptcha Solved!')
            break
        except NoSuchElementException:
            if wait <= 0:
                print('\nCaptcha not solved. Exiting')
                return
            time.sleep(1)
            wait -= 1
            continue

    Student.save_student(student)

    print('Complete')
