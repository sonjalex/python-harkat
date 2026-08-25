import math

##Pyydä ympyrän säde ja tallenna muuttujaan
säde = float(input("Mikä on ympyrän säde? "))
radius_float = float(säde)

##Laske ympyrän pinta-ala
pintaala = (math.pi * radius_float**2)

##Tulosta pinta-ala
print(f"Jos ympyrän säde on {säde: .2f}, sen pinta-ala on {pintaala: .2f}")