from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import Student


def apply(driver, student):
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "ctl00_mainContent_LoggedInFromPublicComputer"))
    ).click()

    try:
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//*[contains(text(),'Log Out')]"))
        ).click
    except TimeoutException:
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.ID, "ctl00_mainContent_CreateUserControl_ProspectForm_firstname_firstname"))
        ).send_keys(student.firstName)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "ctl00_mainContent_CreateUserControl_ProspectForm_lastname_lastname"))
    ).send_keys(student.lastName)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "ctl00_mainContent_CreateUserControl_ProspectForm_emailaddress1_emailaddress1"))
    ).send_keys(student.email)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "ctl00_mainContent_CreateUserControl_ProspectForm_datatel_emailaddress1_confirm_datatel_emailaddress1_confirm"))
    ).send_keys(student.email)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID,
                                    "ctl00_mainContent_CreateUserControl_ProspectForm_address1_telephone1_address1_telephone1"))
    ).send_keys(student.phone)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID,
                                    "ctl00_mainContent_CreateUserControl_ProspectForm_address1_line1_address1_line1"))
    ).send_keys(student.streetAddress)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID,
                                    "ctl00_mainContent_CreateUserControl_ProspectForm_address1_city_address1_city"))
    ).send_keys(student.cityAddress)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID,
                                    "ctl00_mainContent_CreateUserControl_ProspectForm_address1_postalcode_address1_postalcode"))
    ).send_keys(student.postalCode)

    Select(driver.find_element_by_id('ctl00_mainContent_CreateUserControl_ProspectForm_datatel_stateprovinceid_datatel_stateprovinceid')).select_by_visible_text('Pennsylvania')

    Select(driver.find_element_by_id('ctl00_mainContent_CreateUserControl_ProspectForm_datatel_anticipatedentrytermid_datatel_anticipatedentrytermid')).select_by_visible_text('Spring 2021 Credit')

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'ctl00_mainContent_CreateUserControl_ProspectForm_membership_password_membership_password'))
    ).send_keys(student.password)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'ctl00_mainContent_CreateUserControl_ProspectForm_membership_confirmpassword_membership_confirmpassword'))
    ).send_keys(student.password)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'ctl00_mainContent_CreateUserControl_ProspectForm_membership_passwordquestion_membership_passwordquestion'))
    ).send_keys('Mother\'s maiden name')

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'ctl00_mainContent_CreateUserControl_ProspectForm_membership_passwordanswer_membership_passwordanswer'))
    ).send_keys('Doe')

    time.sleep(1)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "ctl00_mainContent_CreateUserControl_CreateUserButton"))
    ).click()

    print(' (Complete)\nSaving student info', end='')

    Student.save_student(student)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'Account Pending Activation')]"))
    )

    print(' (Complete)\nWaiting 3 minutes for email, this may take awhile.')

    continue_app(driver, student)


def continue_app(driver, student: Student.Student):

    driver.get('https://generator.email/' + student.email)

    wait = 180
    while True:
        mins, secs = divmod(wait, 60)
        timeformat = '\rWaiting {:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='')
        try:
            driver.find_element_by_xpath("//*[contains(text(),'Click to Activate Your Account')]")
            print('\rGot the email, continuing')
            break
        except NoSuchElementException:
            if wait <= 0:
                print('\nTimeout reached, run bot.py again in a few hours and continue application')
                return
            time.sleep(1)
            wait -= 1
            continue

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Click to Activate Your Account"))
    ).click()

    time.sleep(1)
    driver.switch_to_window(driver.window_handles[1])

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "ctl00_LoginStatus"))
    ).click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "ctl00_mainContent_LoggedInFromPublicComputer"))
    ).click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "ctl00_mainContent_LoginControl_UserName"))
    ).send_keys(student.email)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "ctl00_mainContent_LoginControl_Password"))
    ).send_keys(student.password)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "ctl00_mainContent_LoginControl_Login"))
    ).click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "2. Start an Application"))
    ).click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Start a New Westmoreland Undergraduate Application"))
    ).click()

    print('1/6 - Plans', end='')

    Select(driver.find_element_by_id(
        'ctl00_mainContent_ApplicationForm_ApplicationForm_ApplicationFormControl_w45_new_planningtoattendwccasahighschoolstude_w45_new_planningtoattendwccasahighschoolstude'))\
        .select_by_index(1)

    Select(driver.find_element_by_id(
        'ctl00_mainContent_ApplicationForm_ApplicationForm_ApplicationFormControl_w45_new_earningadegreecertificateordiploma_w45_new_earningadegreecertificateordiploma'))\
        .select_by_index(1)

    Select(driver.find_element_by_id(
        'ctl00_mainContent_ApplicationForm_ApplicationForm_ApplicationFormControl_w45_new_planningtotransferfromwestmoreland_w45_new_planningtotransferfromwestmoreland'))\
        .select_by_index(2)

    Select(driver.find_element_by_id(
        'ctl00_mainContent_ApplicationForm_ApplicationForm_ApplicationFormControl_w45_new_planningtotransfercreditintowestmorel_w45_new_planningtotransfercreditintowestmorel'))\
        .select_by_index(1)

    Select(driver.find_element_by_id(
        'ctl00_mainContent_ApplicationForm_ApplicationForm_ApplicationFormControl_w45_preferdayoreveningcourses_w45_preferdayoreveningcourses'))\
        .select_by_index(random.randint(0, 3))

    Select(driver.find_element_by_id(
        'ctl00_mainContent_ApplicationForm_ApplicationForm_ApplicationFormControl_w45_parentguardian1highestlevelofeducation_w45_parentguardian1highestlevelofeducation')).select_by_index(random.randint(1, 6))

    Select(driver.find_element_by_id(
        'ctl00_mainContent_ApplicationForm_ApplicationForm_ApplicationFormControl_w45_parentguardian2highestlevelofeducation_w45_parentguardian2highestlevelofeducation')).select_by_index(random.randint(1, 6))

    Select(driver.find_element_by_id(
        'ctl00_mainContent_ApplicationForm_ApplicationForm_ApplicationFormControl_w45_new_areyouinterestedinact101ortrio_w45_new_areyouinterestedinact101ortrio')).select_by_index(1)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "ctl00$mainContent$ApplicationForm$ApplicationForm$ctl01"))
    ).click()

    print(' (Success)\n2/6 - Personal', end='')

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "ctl00_mainContent_ApplicationForm_ApplicationForm_ApplicationFormControl_datatel_ssn_datatel_ssn"))
    ).send_keys(student.ssn)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.ID, "ctl00_mainContent_ApplicationForm_ApplicationForm_ApplicationFormControl_datatel_birthdate_datatel_birthdate"))
    ).send_keys(f'{student.birthdayMonth}/{student.birthdayDay}/{student.birthdayYear}')

    Select(driver.find_element_by_id('ctl00_mainContent_ApplicationForm_ApplicationForm_ApplicationFormControl_datatel_genderid_datatel_genderid')).select_by_index(1)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "ctl00_mainContent_ApplicationForm_ApplicationForm_ApplicationFormControl_w45_primaryphone_w45_primaryphone"))
    ).send_keys(student.phone)

    Select(driver.find_element_by_id('ctl00_mainContent_ApplicationForm_ApplicationForm_ApplicationFormControl_w45_primaryphonetype_w45_primaryphonetype')).select_by_index(2)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "ctl00$mainContent$ApplicationForm$ApplicationForm$ctl01"))
    ).click()

    print(' (Success)\n3/6 - Demographics', end='')

    Select(driver.find_element_by_id('ctl00_mainContent_ApplicationForm_ApplicationForm_ApplicationFormControl_datatel_ethnicity_datatel_ethnicity')).select_by_index(2)

    Select(driver.find_element_by_id('ctl00_mainContent_ApplicationForm_ApplicationForm_ApplicationFormControl_w45_race1_w45_race1')).select_by_index(1)

    Select(driver.find_element_by_id('ctl00_mainContent_ApplicationForm_ApplicationForm_ApplicationFormControl_w45_race2_w45_race2')).select_by_index(1)

    Select(driver.find_element_by_id('ctl00_mainContent_ApplicationForm_ApplicationForm_ApplicationFormControl_w45_race3_w45_race3')).select_by_index(1)

    Select(driver.find_element_by_id('ctl00_mainContent_ApplicationForm_ApplicationForm_ApplicationFormControl_w45_race4_w45_race4')).select_by_index(1)

    Select(driver.find_element_by_id('ctl00_mainContent_ApplicationForm_ApplicationForm_ApplicationFormControl_w45_race5_w45_race5'))\
        .select_by_index(2)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "ctl00$mainContent$ApplicationForm$ApplicationForm$ctl01"))
    ).click()

    print(' (Success)\n4/6 - Academics', end='')

    Select(driver.find_element_by_id('ctl00_mainContent_ApplicationForm_ApplicationForm_ApplicationFormControl_w45_lasthighschoolattended_w45_lasthighschoolattended'))\
        .select_by_index(random.randint(1, 900))

    Select(driver.find_element_by_id('ctl00_mainContent_ApplicationForm_ApplicationForm_ApplicationFormControl_w45_tempattendedhsfrommonth_w45_tempattendedhsfrommonth'))\
        .select_by_index(8)

    Select(driver.find_element_by_id(
        'ctl00_mainContent_ApplicationForm_ApplicationForm_ApplicationFormControl_w45_tempattendedhstomonth_w45_tempattendedhstomonth')) \
        .select_by_index(6)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "ctl00_mainContent_ApplicationForm_ApplicationForm_ApplicationFormControl_w45_attendedhsfromyear_w45_attendedhsfromyear"))
    ).send_keys(str(int(student.birthdayYear) - 4))

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "ctl00_mainContent_ApplicationForm_ApplicationForm_ApplicationFormControl_w45_attendedhstoyear_w45_attendedhstoyear"))
    ).send_keys(student.birthdayYear)

    Select(driver.find_element_by_id(
        'ctl00_mainContent_ApplicationForm_ApplicationForm_ApplicationFormControl_w45_new_takenclassesatactc_w45_new_takenclassesatactc')) \
        .select_by_index(1)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "ctl00$mainContent$ApplicationForm$ApplicationForm$ctl01"))
    ).click()

    print(' (Success)\n5/6 - Activities', end='')

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "ctl00_mainContent_ApplicationForm_ApplicationForm_ApplicationFormControl_w45_new_areyouinterestedinnjcaathletics_w45_new_areyouinterestedinnjcaathletics"))
    )

    Select(driver.find_element_by_id(
        'ctl00_mainContent_ApplicationForm_ApplicationForm_ApplicationFormControl_w45_new_areyouinterestedinnjcaathletics_w45_new_areyouinterestedinnjcaathletics')) \
        .select_by_index(1)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "ctl00$mainContent$ApplicationForm$ApplicationForm$ctl01"))
    ).click()

    print(' (Success)\n6/6 - Writing & Signature', end='')

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID,
                                        "ctl00_mainContent_ApplicationForm_ApplicationForm_ApplicationFormControl_datatel_certify1_datatel_certify1_0"))
    ).click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID,
                                        "ctl00_mainContent_ApplicationForm_ApplicationForm_ApplicationFormControl_datatel_certify2_datatel_certify2_0"))
    ).click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID,
                                        "ctl00_mainContent_ApplicationForm_ApplicationForm_ApplicationFormControl_datatel_certify3_datatel_certify3_0"))
    ).click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID,
                                        "ctl00_mainContent_ApplicationForm_ApplicationForm_ApplicationFormControl_datatel_signature_datatel_signature"))
    ).send_keys(student.firstName + ' ' + student.lastName)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID,
                                        "ctl00_mainContent_ApplicationForm_ApplicationForm_submitBtn"))
    ).click()

    print(' (Success)\nSubmitting', end='')

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID,
                                        "ctl00_mainContent_CompletedControl1_applicationCompletedControl"))
    )

    print(" (Success)")

    print("Check the email in a few days")




