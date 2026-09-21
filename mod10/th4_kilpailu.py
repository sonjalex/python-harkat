import random

class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = []
        for i in range(autot):
        pass
    def tunti_kuluu()
        kulje()
    def tulosta_tilanne()
    def kilpailu_ohi()





class Talo:
    def __init__(self, alin, ylin, hissien_maara):
        self.alin = alin # Ominaisuus
        self.ylin = ylin # Ominaisuus
        self.hissit = []
        for i in range(hissien_maara):
            self.hissit.append(Hissi(alin, ylin))
    def aja_hissia(self, hissin_numero, kerros):
        # Siirrä hissin numeroa vastaava hissi kerrokseen
        self.hissit[hissin_numero].siirry_kerrokseen(kerros)
    def palohälytys(self):
        for hissi in self.hissit:
            hissi.siirry_kerrokseen(1)
        print(f"Palohälytys, siirry alimpaan kerrokseen")