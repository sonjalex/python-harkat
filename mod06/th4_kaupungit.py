##Lista
kaupungit = []

##Kysy ensimmäisen kaupungin nimi
paikat = input("Syötä kaupungin nimi: ")

##For loop

for x in range(5):
    paikka = input(f"Syötä {x + 1} kaupungin nimi: ")
    kaupungit.append(paikka)

for kaupunki in kaupungit:
    print(kaupunki)