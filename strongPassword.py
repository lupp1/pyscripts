#Strong Password detector - Automate the Boring Stuff C7
import re
user_input = input('Insert a password to validate: ')
password_regex = re.compile(r'^(?=.*[A-Z].*[A-Z])(?=.*[!@#$&*])(?=.*[0-9].*[0-9])(?=.*[a-z].*[a-z].*[a-z]).{8}$')

def strongPassword():
    global user_input
    mo = password_regex.search(user_input)
    if mo != None:
        return print('Your password is strong enough.')
    else:
        return print('Your password isn\'t string enough!')
strongPassword()