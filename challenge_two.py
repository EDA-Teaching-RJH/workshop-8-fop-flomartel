##REGEX pattern that validates a student ID format

import re

ID = input("What is your student ID number? ")#asks for student ID number
if re.search ("^[a-zA-z]{4}[0-9]{4}$", ID): #makes sure ID number is 4 letters then 4 numbers
    print("Valid")
else:
    print("Invalid")