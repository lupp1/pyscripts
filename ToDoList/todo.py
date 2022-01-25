#!python3
#Todo list
from sys import exit
todo = []

def create_appointment():
    while True:
        apt = input('Insert appointment (Enter to leave): ')
        todo.append(apt)
        if apt == '':
            initialize()
            break
        #show_appointment()

def show_appointment():
    while '' in todo:
        todo.remove('')
    if len(todo) < 1:
        print('You have no appointments for today.')
    else:
        print("Appointments for today: ")
        for k, v in enumerate(todo):
            print(f'{k + 1} - {v}', sep='\n')
    initialize('What else do you wanna do?')

def initialize(message=None):
    if message is None:
        print("What do you wanna do today?", "1 - Create an appointment", 
        "2 - Show appointments", "3 - Exit", sep='\n')
    else:
        print(message)
    user_input = input('Enter a number: ')
    try:
        if int(user_input) == 1:
            create_appointment()
        elif int(user_input) == 2:
            show_appointment()
        elif int(user_input) == 3:
            quit()
    except ValueError:
        print(f'Insert an integer.')
        initialize()

def quit():
    exit()

initialize()

#TODO: Implement GUI     