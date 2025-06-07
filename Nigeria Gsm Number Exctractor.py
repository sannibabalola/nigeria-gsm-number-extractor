# This code extracts Nigerian phone number using regular expression

import pyperclip
import re  # This imports the pyperclip and re
# Creating the Nigerian phone number pattern using regular expression

phoneNum = re.compile(r'''(
                      (\+234|0)         #Country code
                      (\s|\.|-)?        #Optional Separator  
                      (\d{3})           #First three digits
                      (\s|\.|-)?        #Optional Separator  
                      (\d{3})           #Second set of 3  numbers
                      (\s|\.|-)?        #Optional Separator  
                      (\d{4})           #Last set of 4 numbers
                      )''', re.VERBOSE)

# Scanning through the document for the text the matches the pattern defined above
# and formatting the them properly by removing country code
text = pyperclip.paste()
myPhoneNumberList = []
for groups in phoneNum.findall(text):
    # Checking for valid phone number checking if format is (+234 7) or (+234 8) or (+234 9) or(07) or (08) or (09)
    # Skip invalid numbers

    if groups[1] not in ['+234', '0']:  # Invalid country code
        continue

    if groups[3][0] not in ['7', '8', '9']:  # Invalid network prefix
        continue

    print(groups)

    # Create phone number after validation (normalize to local format)
    phoneNumber = '0' + ''.join([groups[3], groups[5], groups[7]])

    myPhoneNumberList.append(phoneNumber)

# Displaying the phone number on separate line
if len(myPhoneNumberList) > 0:
    pyperclip.copy('\n'.join(myPhoneNumberList))
    print('Phone numbers copied to clipboard: ')
    print('\n'.join(myPhoneNumberList))
    print(len(myPhoneNumberList))
else:
    print('No phone number found')
