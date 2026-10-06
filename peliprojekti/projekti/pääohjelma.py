from pelaaja import Pelaaja, Tavara, Ruokakauppa, Hoivattava

tavara1 = Tavara("porkkana")
pelaaja1 = Pelaaja()

def lue_intro():
    try:
        with open("intro.txt", "r", encoding="utf-8") as tiedosto:
            intro = tiedosto.read()
        return intro
    except FileNotFoundError:
        print("Tiedostoa ei löydy.")
    except IOError:
        print("Tiedoston käsittelyssä tapahtui virhe.")

import json

def tallenna_peli():
    tallennus_data = {
        "pelaaja": pelaaja1.käyttäjä,
        "kori": []
    }
    for tavara in pelaaja1.kori:
        tallennus_data["kori"].append(tavara.nimi)

    with open("tallennus.json", "w") as tiedosto:
        json.dump(tallennus_data, tiedosto)

    print("Tallennettu!")

def lataa_peli():
    try:
        with open("tallennus.json", "r") as tiedosto:
            tallennus = json.load(tiedosto)

        pelaaja1.käyttäjä = tallennus["käyttäjä"]

        pelaaja1.kori = []

        for tavara in tallennus["tavarat"]:
            if tavara == "porkkana":
                pelaaja1.kori.append(tavara1)

        print("Peli ladattu!")

    except FileNotFoundError:
        print("Tallennusta ei löytynyt")

pelaaja1 = Pelaaja()

pelaaja1.käyttäjä()
pelaaja1.ikä()
tallenna_peli()

pelaaja1 = Hoivattava

pelaaja1.hoivattava()
tallenna_peli()

pelaaja1 = Pelaaja

pelaaja1.ruoka()
tallenna_peli()

pelaaja1 = Pelaaja

käyttäjä = input("Syötä pelaajan nimi: ")
print(f"\nHei {käyttäjä} tervetuloa!")
ikä = int(input("Syötä pelaajan ikä: "))


if ikä >= 12:
    print(f"Ikäsi on {ikä}.")
else:
    print("Olet alaikäinen.")


käyttäjä = input("Hei! Mikä on nimesi? ")
print("Hauska tavata, " + käyttäjä + "!")
ikä = int(input("Kerrotko vielä ikäsi: "))

def lue_intro():
    try:
        with open("intro.txt", "r", encoding="utf-8") as tiedosto:
            intro = tiedosto.read()
        return intro
    except FileNotFoundError:
        print("Tiedostoa ei löydy.")
    except IOError:
        print("Tiedoston käsittelyssä tapahtui virhe.")

if ikä < 12:
    print("Pelaajan pitää olla vähintään 12 vuotias, peli sammuu")
    exit()
else:
    print(lue_intro())

    # Pelin idea ja tavoite
    # Miten peli toimii
    # Miten sitä pelataan