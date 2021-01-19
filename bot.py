import time
from selenium import webdriver
import Student
from __colleges import CCC, WCC, LCC, MCC, Stockton


def start_bot():
    with open('prefBrowser.txt', 'r') as fp:
        browser = fp.read()

    try:
        # For Chrome
        if browser == 'chrome':
            options = webdriver.ChromeOptions()
            options.add_argument("user-data-dir=./selenium")
            driver = webdriver.Chrome(options=options, executable_path=r'./webdriver/chromedriver')
        # For Firefox
        elif browser == 'firefox':
            # cap = DesiredCapabilities().FIREFOX
            # cap['marionette'] = True
            driver = webdriver.Firefox(executable_path=r'./webdriver/geckodriver')
    except Exception as e:
        time.sleep(0.4)
        print('\nError - ' + str(e))
        return
    
    driver.maximize_window()
    driver.delete_all_cookies()
    return driver


def new_application(college):
    driver = start_bot()
    student = Student.build_student(driver, college)

    url = Student.allColleges.get(student.college).get('url')

    driver.get(url)

    print('Applying to ' + student.college)

    if 'opencccapply' in url:
        CCC.apply(driver, student)
    elif 'westmoreland' in url:
        WCC.apply(driver, student)
    elif 'lcc' in url:
        LCC.apply(driver, student)
    # elif 'stockton' in url:
    #     Stockton.apply(driver, student)
    # elif 'mcc' in url:
    #     MCC.apply(driver, student)


def continue_application():
    student: Student.Student

    student = Student.get_student_from_file()

    if student is None:
        print('Something bad happened, try again')
        return

    print('Applying as ' + student.firstName + ' ' + student.lastName)

    driver = start_bot()
    WCC.continue_app(driver, student)


def main():
    # Check if setup.py has been run
    with open('prefBrowser.txt', 'r') as fp:
        browser = fp.read()

    if browser == '':
        print('Run setup.py first!')
        return

    print('\nKeep an eye on this console!')
    time.sleep(2)
    print('Select a college:')

    colleges = list(Student.allColleges.keys())
    for index, college in enumerate(colleges):
        print(str(index + 1) + ' - ' + college)

    while True:
        data = input()
        if data == '':
            continue
        if int(data) > len(Student.allColleges) or int(data) < 1:
            print("Invalid response, try again.")
            continue
        else:
            break

    college = colleges[int(data) - 1]

    print('\nSelected College: ' + college)

    if college == 'Westmoreland College':
        print('1 - New Application\n2 - Check email and continue application')

        while True:
            data = input()
            if data == '':
                continue
            if int(data) not in (1, 2):
                print("Invalid response, try again.")
                continue
            else:
                break

        if int(data) == 2:
            continue_application()
            return

    new_application(college)


if __name__ == '__main__':
    main()
