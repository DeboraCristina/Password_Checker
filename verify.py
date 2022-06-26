from sys import argv
from colors import *

def check_pw(s = ''):
    status = []
    if len(s) < 10:
        status.append('w')
    length = len(s) - 1

    c = 0
    for u in s:
        if u.isupper():
            break
        if c == length and not u.isupper():
            status.append('u')
        c += 1

    c = 0
    for l in s:
        if l.islower():
            break
        if c == length and not l.islower():
            status.append('l')
        c += 1

    c = 0
    for d in s:
        if d.isdigit():
            break
        if c == length and not d.isdigit():
            status.append('d')
        c += 1
    return status

def show_error_messages(errors = [], l = 0):
    for error in errors:
        if error == 'w':
            print(f"Short Password. {l} length.")
        elif error == 'u':
            print("No upperrorcase character.")
        elif error == 'l':
            print("No lowerrorcase character.")
        elif error == 'd':
            print("No digit.")

def checker(password = ''):
    status = check_pw(password)
    if not len(status):
        print(f"{GREEN()}OK - \"{password}\"{NC()}")
    else:
        print(f"{RED()}KO - \"{password}\"")
        show_error_messages(status, len(password))
        print(f'{NC()}', end = '')

if len(argv) > 1:
    checker(argv[1])

else:
    print(f"{PURPLE()}Welcome to Password Checker!{NC()}")
    while True:
        print('\n')
        print(f"{BLUE()}What do you want to do?")
        print()
        print(f"(c) Check Password.\n(e) Exit.{NC()}")
        op = input(f"{WHITE()}: ")
        print(f"{NC()}", end = '')
        if op.lower() == 'c':
            checker(input(f"{WHITE()}Password: "))
        else:
            break
        print(f"{NC()}", end = '')
