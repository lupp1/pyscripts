#!python3
# Multiclipboard program - Automate the Boring Stuff C8
# Follow along tutorial.
# Implemented delete keyword
# mcb.pyw - Saves and loads pieces of text to the clipboard
# Command Line Arguments: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword
#                         py.exe mcb.pyw <keyword> - Loads keyword to clipboard
#                         py.exe mcb.pyw list - Loads all keywords to clipboard
#                         py.exe mcb.py delete - Deletes all keys
#                         py.exe mcb.py delete <key> - Delete specific key

import shelve, sys, pyperclip

mcbShelf = shelve.open('mcb')

# Save clipboard content.

if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()

elif len(sys.argv) == 2 and sys.argv[1].lower() == 'delete':
    for key in mcbShelf.keys():
        mcbShelf.pop(key, None)

elif len(sys.argv) >= 2:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
        
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

    elif sys.argv[1].lower() == 'delete' and sys.argv[2] in mcbShelf.keys():
        del mcbShelf[str(sys.argv[2])]
    

    
print(list(mcbShelf.keys()))
mcbShelf.close()
