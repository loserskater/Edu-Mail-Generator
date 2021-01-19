from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import random
import Student


prefix = ['855', '561', '800', '325', '330', '229']


def random_phone_num_generator():
    first = str(random.choice(prefix))
    second = str(random.randint(1, 888)).zfill(3)
    last = (str(random.randint(1, 9998)).zfill(4))
    while last in ['1111', '2222', '3333', '4444', '5555', '6666', '7777', '8888']:
        last = (str(random.randint(1, 9998)).zfill(4))
    return f'({first}) {second}-{last}'


def apply(driver, student):
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Create an Account"))
    ).click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "accountFormSubmit"))
    ).click()

    print('Account Progress - 1/3', end='')

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "inputFirstName"))
    ).send_keys(student.firstName)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "inputMiddleName"))
    ).send_keys(student.middleName)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "inputLastName"))
    ).send_keys(student.lastName)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'hasOtherNameNo'))
    ).click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'hasPreferredNameNo'))
    ).click()

    Select(driver.find_element_by_id(
        'inputBirthDateMonth')) \
        .select_by_value(str(student.birthdayMonth))

    Select(driver.find_element_by_id(
        'inputBirthDateDay')) \
        .select_by_value(str(student.birthdayDay))

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'inputBirthDateYear'))
    ).send_keys(student.birthdayYear)

    Select(driver.find_element_by_id(
        'inputBirthDateMonthConfirm')) \
        .select_by_value(str(student.birthdayMonth))

    Select(driver.find_element_by_id(
        'inputBirthDateDayConfirm')) \
        .select_by_value(str(student.birthdayDay))

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'inputBirthDateYearConfirm'))
    ).send_keys(student.birthdayYear)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, '-have-ssn-yes'))
    ).click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.NAME, 'ssn'))
    ).send_keys(student.ssn)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.NAME, 'ssnConfirm'))
    ).send_keys(student.ssn)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'accountFormSubmit'))
    ).click()

    print(' (Success)')

    print('Account Progress - 2/3', end='')

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'inputEmail'))
    ).send_keys(student.email)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'inputEmailConfirm'))
    ).send_keys(student.email)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'inputSmsPhone'))
    ).send_keys(student.phone)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'inputStreetAddress1'))
    ).send_keys(student.streetAddress)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'inputCity'))
    ).send_keys(student.cityAddress)

    Select(driver.find_element_by_id(
        'inputState')) \
        .select_by_value(str(student.stateAddress))

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'inputPostalCode'))
    ).send_keys(student.postalCode)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'accountFormSubmit'))
    ).click()

    print(' (Success)\nAccount Progress - 3/3')

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'inputUserId'))
    ).send_keys(student.username)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'inputPasswd'))
    ).send_keys(student.password)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'inputPasswdConfirm'))
    ).send_keys(student.password)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'inputPin'))
    ).send_keys(student.pin)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'inputPinConfirm'))
    ).send_keys(student.pin)

    #
    # Question 1
    #

    Select(driver.find_element_by_id(
        'inputSecurityQuestion1')) \
        .select_by_value('5')

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'inputSecurityAnswer1'))
    ).send_keys("John")

    #
    # Question 2
    #

    Select(driver.find_element_by_id(
        'inputSecurityQuestion2')) \
        .select_by_value('6')

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'inputSecurityAnswer2'))
    ).send_keys(student.lastName)

    #
    # Question 3
    #

    Select(driver.find_element_by_id(
        'inputSecurityQuestion3')) \
        .select_by_value('7')

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'inputSecurityAnswer3'))
    ).send_keys("Doe")

    Student.save_student(student)

    print('Please fill the captcha and click Create My Account')

    wait = 180
    while True:
        mins, secs = divmod(wait, 60)
        timeformat = '\rWaiting {:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='')
        try:
            driver.find_element_by_xpath("//*[contains(text(),'Account Created')]")
            print('\rCaptcha Solved!')
            break
        except NoSuchElementException:
            if wait <= 0:
                print('\nCaptcha not solved. Exiting')
                return
            time.sleep(1)
            wait -= 1
            continue

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Continue']"))
    ).click()

    print('Details Progress - 1/8', end='')

    WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.ID, 'inputTermId'))
    )

    Select(driver.find_element_by_id(
        'inputTermId')) \
        .select_by_index(2)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'inputEduGoal'))
    )

    Select(driver.find_element_by_id(
        'inputEduGoal')) \
        .select_by_value('B')

    if student.college == 'Southwestern College':
        Select(driver.find_element_by_id(
            'inputMajorCategory')) \
            .select_by_index(random.randint(1, 12))

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'inputMajorId'))
    )

    Select(driver.find_element_by_id(
        'inputMajorId')) \
        .select_by_index(random.randint(1, 7))

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Continue']"))
    ).click()

    print(' (Success)')

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'inputAddressSame'))
    ).click()

    time.sleep(0.7)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Continue']"))
    ).click()

    print('Details Progress - 2/8', end='')

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'inputEnrollmentStatus'))
    )

    Select(driver.find_element_by_id(
        'inputEnrollmentStatus')) \
        .select_by_index(1)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'inputHsEduLevel'))
    )

    Select(driver.find_element_by_id(
        'inputHsEduLevel')) \
        .select_by_index(1)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'inputHsCompMM'))
    )

    Select(driver.find_element_by_id(
        'inputHsCompMM')) \
        .select_by_value('6')

    Select(driver.find_element_by_id(
        'inputHsCompDD')) \
        .select_by_value(str(student.eduDay))

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'inputHsCompYYYY'))
    ).send_keys(student.eduYear)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'inputCaHsGradYes'))
    ).click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'inputCaHs3yearYes'))
    ).click()

    Select(driver.find_element_by_id(
        'inputHsAttendance')) \
        .select_by_value('1')

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'hs-input-sf-state'))
    )

    Select(driver.find_element_by_id(
        'hs-input-sf-state')) \
        .select_by_value(student.stateAddress)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'hs-school-name'))
    ).send_keys(random.choice(['north', 'east', 'south', 'west']))

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'hs-suggestions'))
    )
    time.sleep(1)

    parent = driver.find_element_by_class_name('autocomplete-menu')
    schools = parent.find_elements_by_tag_name("li")

    schools[random.randint(2, len(schools))].click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'inputGPA'))
    ).send_keys(Keys.BACKSPACE, '400')

    Select(driver.find_element_by_id(
        'inputHighestEnglishCourse')) \
        .select_by_index(random.randint(1, 7))

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'inputHighestEnglishGrade'))
    )

    Select(driver.find_element_by_id(
        'inputHighestEnglishGrade')) \
        .select_by_index(random.randint(1, 8))

    Select(driver.find_element_by_id(
        'inputHighestMathCourseTaken')) \
        .select_by_index(random.randint(1, 13))

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'inputHighestMathTakenGrade'))
    )

    Select(driver.find_element_by_id(
        'inputHighestMathTakenGrade')) \
        .select_by_index(random.randint(1, 8))

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Continue']"))
    ).click()

    print(' (Success)')

    print('Details Progress - 3/8', end='')

    # Military

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'inputCitizenshipStatus'))
    )

    Select(driver.find_element_by_id(
        'inputCitizenshipStatus')) \
        .select_by_index(1)

    Select(driver.find_element_by_id(
        'inputMilitaryStatus')) \
        .select_by_index(1)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Continue']"))
    ).click()

    print(' (Success)')

    print('Details Progress - 4/8', end='')

    # Residency

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'inputCaRes2YearsYes'))
    ).click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'inputHomelessYouthNo'))
    ).click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'inputIsEverInFosterCareNo'))
    ).click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Continue']"))
    ).click()

    print(' (Success)')

    print('Details Progress - 5/8', end='')

    # Interests

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'inputEnglishYes'))
    ).click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'inputFinAidInfoNo'))
    ).click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'inputAssistanceNo'))
    ).click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'inputAthleticInterest3'))
    ).click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Continue']"))
    ).click()

    print(' (Success)')

    print('Details Progress - 6/8', end='')

    # Demographic

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'inputGender'))
    )

    Select(driver.find_element_by_id(
        'inputGender')) \
        .select_by_value('Male')

    Select(driver.find_element_by_id(
        'inputTransgender')) \
        .select_by_value('No')

    Select(driver.find_element_by_id(
        'inputOrientation')) \
        .select_by_value('StraightHetrosexual')

    Select(driver.find_element_by_id(
        'inputParentGuardianEdu1')) \
        .select_by_index(random.randint(1, 7))

    Select(driver.find_element_by_id(
        'inputParentGuardianEdu2')) \
        .select_by_index(random.randint(1, 7))

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'inputHispanicNo'))
    ).click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'inputRaceEthnicity800'))
    ).click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'inputRaceEthnicity' + str(random.randint(801, 809))))
    ).click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Continue']"))
    ).click()

    print(' (Success)')

    print('Details Progress - 7/8', end='')

    # Supplemental

    if student.college == 'Mendocino College':
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'YESNO_1_yes'))
        ).click()

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'YESNO_2_no'))
        ).click()

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'YESNO_3_no'))
        ).click()

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'YESNO_4_no'))
        ).click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, '_supp_TEXT_1'))
        ).send_keys("NONE")

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Continue']"))
        ).click()

    elif student.college == 'Antelope Valley College':

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.ID, '_supp_MENU_1'))
        )

        Select(driver.find_element_by_id(
            '_supp_MENU_1')) \
            .select_by_value('B')

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Continue']"))
        ).click()

    elif student.college == 'Southwestern College':

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.ID, 'YESNO_1_no'))
        ).click()

        Select(driver.find_element_by_id(
            '_supp_MENU_5')) \
            .select_by_index(1)

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Continue']"))
        ).click()

    print(' (Success)')

    print('Details Progress - 8/8', end='')

    # Submission

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'inputConsentYes'))
    ).click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'inputESignature'))
    ).click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'inputFinancialAidAck'))
    ).click()

    print(' (Success)')

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'submit-application-button'))
    ).click()

    print('Complete!\nRun check_email.py in a day or two')
