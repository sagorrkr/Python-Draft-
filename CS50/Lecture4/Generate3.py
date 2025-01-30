import random

number = random.randint(1,10)
print(number)

cards = ["Jack", "King", "Queen"]
random.shuffle(cards)

print(cards)

for card in cards:
    print(card)