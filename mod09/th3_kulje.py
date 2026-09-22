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


auto1 = Auto("ABC-123", 142)

auto1.matka = 2000
auto1.nopeus = 60

auto1.kulje(1.5)

auto1.auto()