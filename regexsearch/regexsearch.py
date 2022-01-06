#  Regex Search
#  Opens all .txt files in a folder and searches for any
#  line that matches a user-supplied regular expression

import os, os.path, re

user_path = input('Enter the path for the folder: ')
user_input = input('Insert a pattern: ')

# Opens all .txt files in a folder

def find_patterns():
    i = 0
    os.path.join(user_path)
    for file in os.listdir(user_path):
        with open(file, 'r') as f:
            content = f.read()
            match = re.search(regEx(), content)
            if match:
                i += 1
    return print(f'A total of {i} matches were found in {user_path}')

def regEx():    
    regex = re.compile(r'{}'.format(user_input))
    return regex

find_patterns()