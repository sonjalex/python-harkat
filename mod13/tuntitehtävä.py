# Aku Ankka (päätoimittaja Aki Hyyppä)
# Hytti n:o 6 (kirjailija Rosa Liksom, 200 sivua)

# Julkaisulla on aina nimi
# Kirjalla on myös kirjoittaja ja sivumäärä
# Lehdellä on myös päätoimittaja

# Tee metodi tulosta_tiedot

# Tulosta tiedot

class Julkaisu:

    def __init__(self, nimi, onko_lainassa = False):
        self.nimi = nimi
        self.onko_lainassa = onko_lainassa

    def onko_lainassa(self, laina):
        False

class Kirja(Julkaisu):

    def __init__(self, nimi, kirjoittaja, sivut):
        super().__init__(nimi)
        self.kirjoittaja = kirjoittaja
        self.sivut = sivut

    def tulosta_tiedot(self):
        pass
        

class Lehti(Julkaisu):

    def __init__(self, nimi, päätoimittaja):
        super().__init__(nimi)
        self.päätoimittaja = päätoimittaja

    def tulosta_tiedot(self):
        pass

kirja1 = Kirja("Hytti n:o 6", "Rosa Liksom", 200)
lehti1 = Lehti("Aku Ankka", "Aki Hyyppä")