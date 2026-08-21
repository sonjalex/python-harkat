import math

##Kysy suorakulmion kanta
kanta = float(input("Mikä on suorakulmion kanta? "))

##Kysy suorakulmion korkeus
korkeus = float(input("Entä sen korkeus? "))

##Laske suorakulmion piiri
piiri = (kanta + korkeus + kanta + korkeus)

##Laske suorakulmion pinta-ala
pintaala = (kanta * korkeus)

##Tulosta vastaukset
print(f"Suorakulmion piiri on {piiri}, ja sen pinta-ala on {pintaala}")