import random

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0
    def auto(self):
        print(f"Rekisteritunnus {self.rekisteritunnus}, huippunopeus {self.huippunopeus} km/h, tämänhetkinen nopeus {self.nopeus} km/h ja kuljettu matka {self.matka:.0f} km")
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

class Kilpailu:
    def __init__(self, nimi, kilometrit, autolista):
        self.nimi = nimi
        self.kilometrit = kilometrit
        self.autolista = autolista

    def tunti_kuluu(self):
        for auto in self.autolista:
            muutos = random.randint(-10,15)
            auto.kiihdytä(muutos)
            auto.kulje(1)

    def tulosta_tilanne(self):
        print(self.nimi)
        for auto in self.autolista:
            auto.auto()

    def kilpailu_ohi(self):
        for auto in self.autolista:
            if auto.matka >= self.kilometrit:
                return True
        return False

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

kilpailu = Kilpailu("Suuri romuralli", 8000, autot)

tunnit = 0

while not kilpailu.kilpailu_ohi():
    kilpailu.tunti_kuluu()
    tunnit += 1

    if tunnit % 10 == 0:
        print(f"Aikaa kulunut: {tunnit} tuntia")
        kilpailu.tulosta_tilanne()

print("Kilpailu on päättynyt, tässä tulokset: ")
järjestetyt_autot = sorted(kilpailu.autolista, key=lambda auto: auto.matka, reverse=True)
for auto in järjestetyt_autot:
    print(f"Rekisteritunnusunnus: {auto.rekisteritunnus}, huippunopeus: {auto.huippunopeus} km/h, matka: {auto.matka} km")