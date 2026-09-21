class Pelihahmo:
    def __init__(self, nimi):
        self.nimi = nimi
        self.pisteet = 0
        self.tavarat = []

ekahahmo = Pelihahmo(input("Anna nimi: "))
print (f"Hahmon {ekahahmo.nimi} pisteet: {ekahahmo.pisteet}")
ekahahmo.pisteet += 1
print (f"Nyt pisteitä on {ekahahmo.pisteet}")