import math
import random

##n pisteiden kokonaismäärä

n = int(input("Kuinka monta pistettä? "))

z = 0
ympyrässä = 0

while z < n:
    y = random.randint(-1000,1000)/1000
    x = random.randint(-1000,1000)/1000

    print(x,y)

##Toteutuuko yhtälö x^2+y^2<1

    if x*x + y*y < 1:
        ympyrässä = ympyrässä + 1

    z = z + 1

pii = 4 * ympyrässä / n

print(f"Likiarvo on: {pii}")