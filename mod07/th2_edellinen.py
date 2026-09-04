import random

##Funktio, joka palauttaa satunnaisen nopan silmäluvun väliltä 1-6

def noppa(tahkot):
    heitto = random.randint(1,tahkot)
    return heitto

##Kysy käyttäjältä nopan maksimi silmäluku

max = int(input("Maksimisilmäluku: "))

##Heittää noppaa kunnes tulos on maksimi
##Tulostaa joka heiton jälkeen saadun silmäluvun

tulos = noppa(max)

while tulos != max:
    print(tulos)
    tulos = noppa(max)

##Tai
##while True:
##  tulos = noppa(tahkot)
##  print(tulos)
##  if tulos == max:
##      break