import re

email = input("What's your email? ").strip()

if re.search(r"^(\w|\.)+@(\w\.)?\w+\.edu$", email, re.IGNORECASE): # (\w|\.) => (a-zA-Z0-9_\.) 
    print("Valid")
else:
    print("Invalid")