# -*- coding: utf-8 -*-
#Finding all phone numbers and e-mail addresses on a clip board.
#This is a sample code of the book whose title is 'Automate the Boreing staff
# with python-Practical Programming for Total Beginners'.
import pyperclip,re

#Making regular expression of phone number

#Bellow is a code for US and Canada's phone number
#phone_regex = re.compile(r'''(
#        (\d{3}|\(\d{3}\))?
#        (\s|-|\.)?
#        (\d{3})
#        (\s|-|\.)
#        (\d{4})
#        (\s*(ext|x|ext.)\s*(\d{2.5}))?
#        )''',re.VERBOSE)

phone_regex = re.compile(r'''(
        (\d{1,4}|\(d{1,4}\))
        (\s|-)
        (\d{1,4})
        (\s|-)
        (\d{3,4})
        (\s*(ext|x|ext.)\s*(\d{2,5}))?
        )''',re.VERBOSE)


#To do Makinge regular expression of E-mail
email_regex = re.compile('''(
        [a-zA-Z0-9._%+-]+
        @
        [a-zA-Z0-9._%+-]+
        (\.[a-zA-Z]{2,4})
        )''',re.VERBOSE)

#To do Searching text of clip board
text = str(pyperclip.paste())
matches = []
for groups in phone_regex.findall(text):
    phone_num = '-'.join([groups[1],groups[3],groups[5]])
    if groups[8] != '':
        phone_num += ' X' + groups[8]
    matches.append(phone_num)
for groups in email_regex.findall(text):
    matches.append(groups[0])

#To do Pasting result of searching to clip board
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Text was printed to clip board.')
    print('\n'.join(matches))
else:
    print('Phone number or E-mail could not be found.')
    