kori = []

class Ruokakauppa:
    def __init__(self, ikä, ruoka, tulosta):
        super().__init__(ikä)
        self.ikä = ikä
        self.ruoka = ruoka
        self.tulosta = tulosta
        self.kori = []

    def ruoka():
        ruokia = input("Menet eläinkauppaan etsimään lemmikillesi ruokaa, mitä valitset hyllystä? (tyhjä lopettaa) ")
        while ruokia != "":
            kori.append(ruokia)
            print(f"{ruokia} on lisätty ostoskoriin")
            ruokia = input("Lisää ruoka koriisi (tyhjä lopettaa): ")

    def tulosta():
        if len(kori) == 0:
            print("Ostoskorissasi ei ole mitään! Ethän jätä lemmikkiäsi ruokkimatta?")
        else:
            print("Ostoskorissasi on:")
            for ruoat in kori:
                print(">", ruoat)

class Tavara:
    def __init__(self, nimi):
        self.nimi = nimi

class Pelaaja(Ruokakauppa):
    def __init__(self, nimi, käyttäjä, ikä):
        self.nimi = nimi
        self.käyttäjä = käyttäjä
        self.ikä = ikä
        self.kori = []

import random

eläimiä = ["kissa", "koira", "hamsteri", "hevonen"]

class Hoivattava:
    def __init__(self, hoivattava, arvottu_hoivattava):
        self.hoivattava = hoivattava
        self.arvottu_hoivattava = arvottu_hoivattava

    def hoivattava():
        print("\nTässä on lista eläimistä joista saat yhden satunnaisesti hoidettavaksesi: ")
        for eläin in eläimiä:
            print(">", eläin)
        arvottu_hoivattava = random.choice(eläimiä)
        print(f"\nSinulla on: {arvottu_hoivattava}")