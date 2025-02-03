import re

email = input("Whats's your email?").strip()
if re.search(r"^[^@]+@[^@]+\.edu$", email): # ^starting and $ ending, []set of characters [^]cpmplementing the set
    print("Valid")
else:
    print("Invalid")