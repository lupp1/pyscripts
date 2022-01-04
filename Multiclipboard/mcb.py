#!python3
# Multiclipboard program - Automate the Boring Stuff C8
# Follow along tutorial.
# mcb.pyw - Saves and loads pieces of text to the clipboard
# Command Line Arguments: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword
#                         py.exe mcb.pyw <keyword> - Loads keyword to clipboard
#                         py.exe mcb.pyw list - Loads all keywords to clipboard

import shelve, sys, pyperclip

mcbShelf = shelve.open('mcb')

# Save clipboard content.
# Checks for lenght of sys.argv list, checks keyword - i.e 'save'.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    # List keywords and load content.
    # Checks for remaining keywords, i.e 'list' and copies content to clipboard as str value.
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    # Otherwise, assume the CLA is a keyword.
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
mcbShelf.close()
