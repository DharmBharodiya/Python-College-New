import re

password = input("Enter your password")
# pattern = r"^([a-z]+[A-Z]+[$#@]+[0-9]+){6,12}$"
pattern = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[#@$])[A-Za-z\d$#@]{6,12}$"

match = re.search(pattern, password)
if match:
    print("Logged In")
else:
    print("Invalid Password")