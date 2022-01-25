import re
'''RegEx version of the built-in function strip()
Used to remove whitespaces at the start/end of a string'''

x = input('Insert a string for strip(): ')

def regex_strip(string):
    pattern = '(^\s*)|(\s*$)'
    regex = re.sub(pattern, '', string)
    return regex

print(regex_strip(x))
