import os
import webbrowser
from time import sleep

emails = ["Check All"]


def get_emails():
    with open('students.txt', 'r') as f:
        accounts = f.readlines()

    for line in accounts:
        emails.append(line.split('"college": "')[1].split('"')[0] + ' - ' + line.split('"email": "')[1].split('"')[0])


def main():
    if os.stat('students.txt').st_size == 0:
        print('No accounts created yet, run bot.py')
        return

    get_emails()

    print("Select an email to check:")

    for index, email in enumerate(emails):
        print(str(index) + ' - ' + email)

    while True:
        data = int(input())
        if data > len(emails) or data < 0:
            print("Invalid response, try again.")
            continue
        else:
            break
    if data == 0:
        emails.pop(0)
        webbrowser.open('https://generator.email/')
        sleep(10)
        for email in emails:
            webbrowser.open('https://generator.email/'+email.split(' - ')[1], new=2)
            sleep(5)
    else:
        webbrowser.open('https://generator.email/' + emails[data].split(' - ')[1])


if __name__ == '__main__':
    main()
