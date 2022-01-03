#Todo list
from sys import exit
todo = []

def create_appointment():
    while True:
        apt = input('Insert appointment: (Enter to leave)')
        todo.append(apt)
        if apt == '':
            break
        #show_appointment()

def show_appointment():
    while '' in todo:
        todo.remove('')
    if len(todo) < 1:
        print('You have no appointments for today.')
    else:
        for k, v in enumerate(todo):
            print("Appointments for today: ", k + ' - ' + v, sep='\n')
    initialize('What else do you wanna do?')

def initialize(message=None):
    if message == None:
        print("What do you wanna do today?", "1 - Create an appointment", 
        "2 - Show appointments", "3 - Exit", sep='\n')
    else:
        print(message)
    user_input = int(input('Enter a number: '))
    try:
        if user_input == 1:
            create_appointment()
        elif user_input == 2:
            show_appointment()
        elif user_input == 3:
            quit()
    except ValueError as err:
        print('(ERROR) Type an integer: ')
        initialize()

def quit():
    exit()

initialize()

#TODO: Implement GUI     