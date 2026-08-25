##Kolminumeroinen koodi, jonka kukin numeromerkki on väliltä 0-9
import random
print(random.sample(range(0, 9), 3))
##Nelinumeroinen koodi, jonka kukin numeromerkki on väliltä 1-6
print(random.sample(range(1, 6), 4))

##Tai random.radintin kanssa

luku01 = int(random.randint(0,9))
luku02 = int(random.randint(0,9))
luku03 = int(random.randint(0,9))
print(luku01, luku02, luku03)

luku1 = int(random.randint(1,6))
luku2 = int(random.randint(1,6))
luku3 = int(random.randint(1,6))
luku4 = int(random.randint(1,6))
print(luku1, luku2, luku3, luku4)