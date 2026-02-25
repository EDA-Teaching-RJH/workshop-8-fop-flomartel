import re
number = input("What is your phone number? ")
if re.search("^07\d{9}$", number):
    print("Valid")
else:
    print("Invalid")