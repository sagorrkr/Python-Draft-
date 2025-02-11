"""first, last = input("What's your name?").split(" ")
print(f"Hello, {first}")"""

def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts

print(total(100, 50, 25), "Knuts")