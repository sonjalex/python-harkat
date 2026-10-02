kori = []

class Ruokakauppa:
    def __init__(self, ikä, ruoka, tulosta):
        super().__init__(ikä)
        self.ikä = ikä
        self.ruoka = ruoka
        self.tulosta = tulosta

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