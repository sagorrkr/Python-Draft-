class Vault():
    def __init__(self, galleons = 0, sickeles = 0, knuts = 0):
        self.galleons = galleons
        self.sickeles = sickeles
        self.knuts = knuts

    def __str__(self):
        return f"{self.galleons} Galleons, {self.sickeles} Sickeles, {self.knuts} Knuts"
    
    def __add__(self, other):
        galleons = self.galleons + other.galleons
        sickeles = self.galleons + other.galleons
        knuts = self.knuts + other.knuts
        return Vault(galleons, sickeles, knuts)

potter = Vault(100, 50, 25)
print(potter)

weasley = Vault(25, 50, 100)
print(weasley)

total = potter + weasley
print(total)