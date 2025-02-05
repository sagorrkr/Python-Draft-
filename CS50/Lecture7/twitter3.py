import re

url = input("URL: ").strip()
# := or-else operator
if  matches := re.search(r"^https?://?(?:www\.)?twitter\.com/([/w]+)", url, re.IGNORECASE): #?: is to escape()
    print(f"Username: ", matches.group(1))

