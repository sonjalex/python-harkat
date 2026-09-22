import random

class Kilpailu:
    def __init__(self, nimi, kilometrit):
        self.nimi = nimi
        self.kilometrit = kilometrit
        self.nopeus = 0
        self.autolista = [auto1, auto2, auto3, auto4, auto5, auto6, auto7, auto8, auto9, auto10]
        auto1 = Kilpailu("ABC-1")
        auto2 = Kilpailu("ABC-2")
        auto3 = Kilpailu("ABC-3")
        auto4 = Kilpailu("ABC-4")
        auto5 = Kilpailu("ABC-5")
        auto6 = Kilpailu("ABC-6")
        auto7 = Kilpailu("ABC-7")
        auto8 = Kilpailu("ABC-8")
        auto9 = Kilpailu("ABC-9")
        auto10 = Kilpailu("ABC-10")
    def auto(self, autot):
        self.autolista.append(autot)
        return
    def kiihdytä(self, kiihtyminen):
            self.nopeus += kiihtyminen
            if self.nopeus > self.huippunopeus:
                self.nopeus = self.huippunopeus
            if self.nopeus < 0:
                self.nopeus = 0
    def kulje(self, tunti):
            self.matka += self.nopeus * tunti
    def tunti_kuluu():
        while Kilpailu:
            for auto in Kilpailu:
                nopeus = random.randint(-10, 15)
                auto.kiihdytä(nopeus)
                matka += nopeus * 1
                auto.kulje(1)
    def tulosta_tilanen():
        pass
    def kilpailu_ohi():
        pass


Kilpailu.self.autolista()