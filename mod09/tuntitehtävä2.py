import random

# Luo luokka ja sinne lista
class Loitsuja:
    def __init__(self, nimi):
        self.nimi = nimi

class Loitsut:
    def __init__(self):
        self.loitsut = []

    def lisaa_loitsu(self, loitsu):
        self.loitsut.append(loitsu)
        print(loitsu.nimi + "loitsu lisätty")
        return

loitsu1 = Loitsuja("Jää")
loitsu2 = Loitsuja("Pallosalama")

loitsut = Loitsut()

loitsut.lisaa_loitsu(loitsu1)
loitsut.lisaa_loitsu(loitsu2)