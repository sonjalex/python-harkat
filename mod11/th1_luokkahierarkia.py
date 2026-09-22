# Aku Ankka (päätoimittaja Aki Hyyppä)
# Hytti n:o 6 (kirjailija Rosa Liksom, 200 sivua)

# Julkaisulla on aina nimi
# Kirjalla on myös kirjoittaja ja sivumäärä
# Lehdellä on myös päätoimittaja

# Tee metodi tulosta_tiedot

# Tulosta tiedot

class Julkaisu:

    def __init__(self, nimi):
        self.nimi = nimi

class Kirja(Julkaisu):

    def __init__(self, nimi, kirjoittaja, sivut):
        super().__init__(nimi)
        self.kirjoittaja = kirjoittaja
        self.sivut = sivut

    def tulosta_tiedot(self):
        print(f"Nimi: {self.nimi}, Kirjoittaja: {self.kirjoittaja}, Sivumäärä: {self.sivut}")

class Lehti(Julkaisu):

    def __init__(self, nimi, päätoimittaja):
        super().__init__(nimi)
        self.päätoimittaja = päätoimittaja

    def tulosta_tiedot(self):
        print(f"Nimi: {self.nimi}, Päätoimittaja: {self.päätoimittaja}")

kirja1 = Kirja("Hytti n:o 6", "Rosa Liksom", 200)
lehti1 = Lehti("Aku Ankka", "Aki Hyyppä")

kirja1.tulosta_tiedot()
lehti1.tulosta_tiedot()