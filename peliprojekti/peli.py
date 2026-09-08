import random

nimi = input("Syötä pelaajan nimi: ")
ikä = int(input("Syötä pelaajan ikä: "))

if ikä >= 12:
    print(f"\nHei {nimi} tervetuloa! Ikäsi on {ikä}.")

else:
    print("Olet alaikäinen.")

eläimiä = ["kissa", "koira", "hamsteri", "hevonen"]

def hoivattava():
    print("\nTässä on lista eläimistä joista saat yhden satunnaisesti hoidettavaksesi: ")
    for eläin in eläimiä:
        print(">", eläin)

    arvottu = random.choice(eläimiä)
    print(f"\nSinulla on: {arvottu}")

kori = []

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

def ohjeita():
    print("\nOhjeet\n\nPelin tarkoituksena on pitää huolta saamastasi lemmikistä! Valitse lemmikillesi sopiva peti, ruoka ja aktiviteetit voittaaksesi pelin.\n\nPeli valitsee satunnaisesti lemmikin sinulle - tässä on lista mahdollisista eläimistä: \n")
    for eläin in eläimiä:
        print(">", eläin)

while ikä > 11:
    print("\nPäävalikko \n\nAloita peli \nOhjeet \nLopeta")

    komento = input("\nAnna komento: ")

    if komento == "lopeta":
        break

    if komento == "aloita":
        print("\nOle paras lemmikinomistaja!")
        hoivattava()
        ruoka()
        tulosta()
        komento = input("\nPalaa takaisin päävalikkoon k/e: ")

        if komento == "e":
            break

    if komento == "ohjeet":
        ohjeita()
        komento = input("\nPalaa takaisin päävalikkoon k/e: ")

        if komento == "e":
            break
    else:
        print("Käytäthän komentona sanoja: aloita, ohjeet tai lopeta")

print("Toiminto lopetettu")