##Kysy maalattavan seinän korkeus ja leveys sekä maalin maalattavan pinta-alan litraa kohti
korkeus = float(input("Mikä on maalattavan seinän korkeus? "))
leveys = float(input("Entä sen leveys? "))
kattavuus = float(input("Anna kattavuus "))
##Tulosta kuinka paljon maalia tarvitaan
pintaala = (korkeus * leveys)
maalin_tarve = (pintaala / kattavuus)

print(f"Maalia tarvitaan {maalin_tarve} litraa maalaamiseen.")