from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import random
import Student


def apply(driver, student):
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "login_id"))
    ).send_keys(student.username)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "pin_id"))
    ).send_keys(student.pin)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "verify_pin_id"))
    ).send_keys(student.pin)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "id____UID0"))
    ).click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "app_type_id"))
    )

    Select(driver.find_element_by_id('app_type_id')).select_by_index(1)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "id____UID0"))
    ).click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "term_id"))
    )

    Select(driver.find_element_by_id('term_id')).select_by_index(2)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "first_id"))
    ).send_keys(student.firstName)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "last_id"))
    ).send_keys(student.lastName)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "id____UID0"))
    ).click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Name"))
    ).click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "lname_id"))
    )

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "id____UID1"))
    ).click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "addr1_id"))
    ).send_keys(student.streetAddress)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "city_id"))
    ).send_keys(student.cityAddress)

    Select(driver.find_element_by_id('stat_id')).select_by_value(student.stateAddress)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "zip_id"))
    ).send_keys(student.postalCode)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "area_id"))
    ).send_keys(student.phone.split('-')[0])

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "phone_id"))
    ).send_keys(student.phone.split('-')[1:])

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "ud1_yes_id"))
    ).click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "ud2_no_id"))
    ).click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "id____UID1"))
    ).click()

    while True:
        try:
            WebDriverWait(driver, 2).until(
                EC.element_to_be_clickable((By.XPATH, "//*[contains(text(),'(Checklist item 3 of 6)')]"))
            )
            break
        except TimeoutException:
            try:
                WebDriverWait(driver, 2).until(
                    EC.element_to_be_clickable((By.XPATH, "//*[contains(text(),'Errors occurred')]"))
                )
                print("Bad address, trying a new one")
                Student.get_new_address(student)
                temp = driver.find_element_by_id("addr1_id")
                temp.clear()
                temp.send_keys(student.streetAddress)
                temp = driver.find_element_by_id("city_id")
                temp.clear()
                temp.send_keys(student.cityAddress)
                Select(driver.find_element_by_id('stat_id')).select_by_value(student.stateAddress)
                temp = driver.find_element_by_id("zip_id")
                temp.clear()
                temp.send_keys(student.postalCode)
                driver.find_element_by_id("id____UID1").click()
            except TimeoutException:
                continue

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[contains(text(),'(Checklist item 3 of 6)')]"))
    )

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "id____UID1"))
    ).click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "citz_id"))
    )

    Select(driver.find_element_by_id('citz_id')).select_by_value('01')

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "email_id"))
    ).send_keys(student.email)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "dup_email_id"))
    ).send_keys(student.email)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "ssn_id"))
    ).send_keys(student.ssn)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "M_gender_id"))
    ).click()

    Select(driver.find_element_by_id('month_id')).select_by_index(int(student.birthdayMonth))

    Select(driver.find_element_by_id('day_id')).select_by_index(int(student.birthdayDay))

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "year_id"))
    ).send_keys(student.birthdayYear)

    if student.stateAddress == 'MI':
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "Y_resd_id"))
        ).click()
    else:
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "N_resd_id"))
        ).click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "ud1_no_id"))
    ).click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "ethn_cat_nothispanic_id"))
    ).click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "race_id5"))
    ).click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "id____UID1"))
    ).click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "school_id"))
    ).send_keys('230000')

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "hs_name_id"))
    ).send_keys('Eastern High School')

    Select(driver.find_element_by_id('gmonth_id')).select_by_index(int(student.eduMonth))

    Select(driver.find_element_by_id('gday_id')).select_by_index(int(student.eduDay))

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "gyear_id"))
    ).send_keys(student.eduYear)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "id____UID2"))
    ).click()

    Select(driver.find_element_by_id('program_id')).select_by_index(random.randint(1, 150))

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "ud1_id"))
    ).send_keys(student.firstName[0] + student.lastName[0])

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "id____UID1"))
    ).click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[contains(text(),'Application is Complete')]"))
    )

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "id____UID0"))
    ).click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "I agree to the terms"))
    ).click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[contains(text(),'" + student.username + "')]"))
    )

    Student.save_student(student)

    print('Complete')


