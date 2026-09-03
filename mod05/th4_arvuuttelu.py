import random

##Random numero 1-10
luku = int(random.randint(1,10))

##Kysy arvausta 1-10
arvaus = int(input("Arvaa luku väliltä 1-10: "))

while arvaus != luku:
    ##Liian pieni arvaus
    if arvaus < luku:
        print("Liian pieni arvaus")
        arvaus = int(input("Arvaa luku väliltä 1-10: "))
    ##Liian suuri arvaus
    if arvaus > luku:
        print("liian suuri arvaus")
        arvaus = int(input("Arvaa luku väliltä 1-10: "))

##Oikea arvaus
print(f"Arvasit oikein! Luku oli {luku}.")