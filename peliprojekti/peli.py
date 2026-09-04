nimi = input("Syötä pelaajan nimi: ")
ikä = int(input("Syötä pelaajan ikä: "))

if ikä >= 12:
    print(f"\nHei {nimi} tervetuloa! Ikäsi on {ikä}.")

else:
    print("Olet alaikäinen.")
    

while ikä > 11:
    print("\nPäävalikko \n\nAloita peli \nOhjeet \nLopeta")
    komento = input("\nAnna komento: ")
    if komento == "lopeta":
        break
    if komento == "aloita":
        print("Peli")
        komento = input("\nPalaa takaisin päävalikkoon k/e: ")
        if komento == "e":
            break
    if komento == "ohjeet":
        print("Ohjeet")
        komento = input("\nPalaa takaisin päävalikkoon k/e: ")
        if komento == "e":
            break
print("Toiminto lopetettu")