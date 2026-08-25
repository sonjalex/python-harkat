##Kysy kolmea kokonaislukua
kokonaisluku1 = float(input("Kerro ensimmäinen kokonaisluku: "))
kokonaisluku2 = float(input("Kerro toinen kokonaisluku: "))
kokonaisluku3 = float(input("Kerro kolmas kokonaisluku: "))

##Laske summa
summa = (kokonaisluku1 + kokonaisluku2 + kokonaisluku3)

##Laske tulo
tulo = (kokonaisluku1 * kokonaisluku2 * kokonaisluku3)

##Laske keskiarvo
keskiarvo = ((kokonaisluku1 + kokonaisluku2 + kokonaisluku3) / 3)

print(f"Lukujen summa on{summa: .2f}, niiden tulo on{tulo: .2f} ja keskiarvo on{keskiarvo: .2f}") 