import pyperclip

change_name = input('Change name: ').title()
change_greet = input('Greet: ').lower()
pyperclip.copy('Olá {}, {}! No momento infelizmente não estou buscando novas oportunidades, '
               'mas agradeço pelo seu contato e tempo para me enviar. Obrigado!'.format (change_name, change_greet))
