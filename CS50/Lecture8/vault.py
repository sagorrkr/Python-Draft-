class Vault():
    def __init__(self, galleons = 0, sickeles = 0, knuts = 0):
        self.galleons = galleons
        self.sickeles = sickeles
        self.knuts = knuts

    def __str__(self):
        return f"{self.galleons} Galleons, {self.sickeles} Sickeles, {self.knuts} Knuts"

potter = Vault(100, 50, 25)
print(potter)

weasley = Vault(25, 50, 100)
print(weasley)


galleons = potter.galleons + weasley.galleons
sickeles = potter.sickeles + weasley.sickeles
knuts = potter.knuts + weasley.knuts

print(galleons)
print(sickeles)
print(knuts)

total = Vault(galleons, sickeles, knuts)

print(total)