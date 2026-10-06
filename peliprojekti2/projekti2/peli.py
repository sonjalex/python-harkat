# Metsäseikkailupeli
# Jos ei karttaa = Väärä reitti
# Jos ei kasvikirjaa = Syö myrkyllisen marjan

# Pelaaja

# Kysytään pelaajan tiedot, jos alle 12 vuotias pääsy evätään
nimi = input("Anna nimesi: ")
print(f"Hei, {nimi}")
ikä = int(input("Syötä ikäsi: "))
print(f"Olet {ikä} vuotias.")
if ikä < 12:
    print("Olet liian nuori, sinun pitää olla vähintään 12 vuotias pelataksesi peliä")
    exit()
else:
    print(f"Seikkailusi metsässä on valmis alkamaan {nimi}!")

# Päävalikko sisältää pelin ohjeet, pelin aloituksen, poistumisen ja aloituksen

class Pelaaja:
    def __init__(self, nimi, reppu, metsä):
        self.nimi = nimi
        self.reppu = reppu
        self.metsä = metsä
class Päävalikko:
    def __init__(self, nimi):
        self.nimi = nimi
    def päävalikko():
        print("\nTervetuloa metsäseikkailuun!\n\nAloita\nJatka\nOhjeet\nLopeta peli")


def ohjeet():
    print("\nTervetuloa metsäseikkailuun!\n\nOlet lähdössä retkelle metsään, lyhyelle eräseikkailulle puiden lomaan. Edessäsi tulee olemaan tärkeitä valintoja, jotka päättävät pelin kulustasi. Toivottavasti metsäseikkailusi on antoisa!\nAloita peli syöttämällä pääävalikossa komentokenttään 'Aloita'\nLue ohjeet syöttämällä päävalikossa komentokenttään 'Ohjeet' (Kiva että löysit tänne ilman ohjeita!)\nLopeta peli syöttämällä päävalikon komentokenttään 'Lopeta'\n\nPalaa päävalikkoon painamalla 'Enter' näppäintä.")


def reitti1():
    print("Kävelet pitkin kaunista maisemareittiä, näät matkallasi erilaisia lintuja ")

def reitti2():
    print("Kävelet pitkin maisemareittiä joka muuttuu äkisti kivikkoiseksi, ")

reittivalinta()