class Päävalikko():
    def __init__(self, ikä, ohjeita, ruoka, tulosta, hoivattava):
        self.ohjeita = ohjeita
        super().__init__(ikä)
        self.ikä = ikä
        super().__init__(ruoka, tulosta)
        self.ruoka = ruoka
        self.tulosta = tulosta
        super().__init__(hoivattava)
        self.hoivattava = hoivattava

    def valikko():
        print("\nPäävalikko \n\nAloita peli \nOhjeet \nLopeta")
        komento = input("\nAnna komento: ")
        if komento == "lopeta":
            pass
    def aloita():
        if komento == "aloita":
            print("\nOle paras lemmikinomistaja!")
            hoivattava()
            ruoka()
            tulosta()
            komento = input("\nPalaa takaisin päävalikkoon k/e: ")
        if komento == "e":
            pass

    def valikko():
        if komento == "ohjeet":
            print("\nOhjeet\n\nPelin tarkoituksena on pitää huolta saamastasi lemmikistä! Valitse lemmikillesi sopiva peti, ruoka ja aktiviteetit voittaaksesi pelin.\n\nPeli valitsee satunnaisesti lemmikin sinulle - tässä on lista mahdollisista eläimistä: \n")
            eläimiä = ["kissa", "koira", "hamsteri", "hevonen"]
            for eläin in eläimiä:
                print(">", eläin)
            komento = input("\nPalaa takaisin päävalikkoon k/e: ")
        if komento == "e":
            pass
        else:
            print("Käytäthän komentona sanoja: aloita, ohjeet tai lopeta")