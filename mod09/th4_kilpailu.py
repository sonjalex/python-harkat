import random

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0
    def auto(self):
        print(f"Auton rekisteritunnus on {self.rekisteritunnus}, huippunopeus {self.huippunopeus} km/h, tämänhetkinen nopeus {self.nopeus} km/h ja kuljettu matka {self.matka:.0f} km")
    def kiihdytä(self, kiihtyminen):
        self.nopeus += kiihtyminen
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        if self.nopeus < 0:
            self.nopeus = 0
    def hätäjarrutus(self):
        self.kiihdytä(-200)
    def kulje(self, tunti):
        self.matka += self.nopeus * tunti

auto1 = Auto("ABC-1", random.randint(100, 200))
auto2 = Auto("ABC-2", random.randint(100, 200))
auto3 = Auto("ABC-3", random.randint(100, 200))
auto4 = Auto("ABC-4", random.randint(100, 200))
auto5 = Auto("ABC-5", random.randint(100, 200))
auto6 = Auto("ABC-6", random.randint(100, 200))
auto7 = Auto("ABC-7", random.randint(100, 200))
auto8 = Auto("ABC-8", random.randint(100, 200))
auto9 = Auto("ABC-9", random.randint(100, 200))
auto10 = Auto("ABC-10", random.randint(100, 200))

autot = [auto1, auto2, auto3, auto4, auto5, auto6, auto7, auto8, auto9, auto10]

kilpailu = True

while kilpailu:
    for auto in autot:
        nopeus = random.randint(-10, 15)
        auto.kiihdytä(nopeus)

        auto.kulje(1)

        if auto.matka >= 10000:
            kilpailu = False

for auto in autot:
    auto.auto()