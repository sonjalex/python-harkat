import random

eläimiä = ["kissa", "koira", "hamsteri", "hevonen"]

class Hoivattava:
    def __init__(self, hoivattava, arvottu_hoivattava):
        self.hoivattava = hoivattava
        self.arvottu_hoivattava = arvottu_hoivattava

    def hoivattava():
        print("\nTässä on lista eläimistä joista saat yhden satunnaisesti hoidettavaksesi: ")
        for eläin in eläimiä:
            print(">", eläin)
        arvottu_hoivattava = random.choice(eläimiä)
        print(f"\nSinulla on: {arvottu_hoivattava}")