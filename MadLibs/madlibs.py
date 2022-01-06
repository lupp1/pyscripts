# MabLibs - reads in text file and lets the user add their own text
# anywhere the word ADJECTIVE, NOUN, VERB or ADVERB appears

# Create a text file write-mode.

import os.path

x = 'The ADJECTIVE puppy walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events.'  

ADJECTIVE = str(input('Enter an adjective: ')) 
NOUN = str(input('Enter a noun: '))
VERB = str(input('Enter a verb: '))

replace_dict = {'ADJECTIVE': ADJECTIVE, 
                'NOUN': NOUN, 
                'VERB': VERB}

def create_write(write_str):

    if os.path.exists('C:.\\MadLibs\\madfile.txt') is not True:
        with open('madfile.txt', 'w') as mad_file:
            mad_file.write(write_str)

    return write_str
    
def replace_with(words):

    for key, val in replace_dict.items():
        words = words.replace(key, val)

    return words
if '__init__' == '__main__':
    print('This is your initial sentence:', x)
    print(replace_with(x))