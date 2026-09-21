class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0
    def auto(self):
        print(f"Auton rekisteritunnus on {self.rekisteritunnus}, huippunopeus {self.huippunopeus} km/h, tämänhetkinen nopeus {self.nopeus} km/h ja kuljettu matka {self.matka:.0f} km")

auto1 = Auto("ABC-123", 142)
auto1.auto()