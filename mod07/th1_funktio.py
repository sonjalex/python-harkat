import random

##Funktio, joka palauttaa satunnaisen nopan silmäluvun väliltä 1-6

def noppa():
    heitto = random.randint(1,6)
    return heitto

##Heittää noppaa kunnes tulos on 6
##Tulostaa joka heiton jälkeen saadun silmäluvun
tulos = noppa()

while tulos != 6:
    print(tulos)
    tulos = noppa()

##Tai
##while True:
##  tulos = noppa()
##  print(tulos)
##  if tulos == 6:
##      break