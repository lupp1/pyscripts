# simple login screen
import shelve

# Testing shelve

emails = []
passwords = []
users_shelf = shelve.open('Users')

# Register user.

def ask_user(message=None): 

    global user_password, user_email # Bad practice - Implement classes as soon as learned 

    if message is None:
        user_email = input('Insert an e-mail: ')
        user_password = input('Create a password: ')

    if message is not None:
        print(message)
        user_password = input('Create a password: ')
        pass

def register():

    emails.append(user_email)
    passwords.append(user_password)
    users_shelf['email'] = emails
    users_shelf['password'] = passwords

# Strong password detector.

def password_strenght(password=None):

    if password == '':
        ask_user('Insert a password.')
    else:
        return (len(password) >= 8
                and password != password.upper()
                and password != password.lower()
                and any(char.isdigit() for char in password))

def check_strenght(strong:bool):

    return (print('Your password is strong.') if password_strenght(user_password) is True 
    else print('Your password isn\'t strong enough. Your password must contain at least: \
            \n8 characters\nOne uppercase and lowercase letter\nOne digit'))

# Check if user exists or not

def check_user(email):

    if email in users_shelf['email']:    
        return print('User already exists'), ask_user()

if __name__ == '__main__':  
    
    ask_user()
    register()
    check_user(user_email)
    check_strenght(password_strenght(user_password))

# TODO: Assign user to a text file or a module, or a database haven't decided yet

# TODO: GUI?