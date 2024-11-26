import re

pattern = r"@[\w.-]+\.(\w+)$"

email = input("Enter your email ID: ")

match = re.search(pattern, email)
if match:
    print(f"The top-level domain (TLD) is: {match.group(1)}")
else:
    print("Invalid email format!")
