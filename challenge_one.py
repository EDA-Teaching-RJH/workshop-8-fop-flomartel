
#REGEX pattern that validates standard UK mobile phone numbers
import re

number = input("What is your phone number? ")
if re.search("^07\d{9}$", number): #makes sure number starts with 07, is decimal digits, and has 9 digits after the 07
    print("Valid")
else:
    print("Invalid")