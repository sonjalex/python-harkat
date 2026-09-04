##Funktio averages
##Ottaa parametrina listan liukulukuja ja palauttaa listan numeroiden keskiarvon
def averages(luvut):
    avg = sum(luvut) / len(luvut)
    return avg
    ##Laske lukujen keskiarvo

##Tai
##summa = 0
##  for luku in luvut:
##      summa += luku

##Funktio average grade
##Ottaa parametrina listan listoja
##Palauttaa listan jossa on jokaisen listan keskiarvo
def average_grade(luvut):
    ##Laske jokaisen listan alkion keskiarvo ja tallenna se listaan
    keskiarvot = []
    for alkio in luvut:
        keskiarvo = averages(alkio)
        keskiarvot.append(keskiarvo)
    ##Tai
    ## keskiarvot.append(averages(alkio))

    return keskiarvot
    ##Palauta uusi lista

##Luodaan lista lukuja
##Lasketaan lukujen keskiarvo
lista = [{1, 5, 43, 6.6}, {25, 2.4, 60, 7.8}]
keskiarvot = average_grade(lista)

##Tulostetaan keskiarvot
for keskiarvo in keskiarvot:
    print(f"Keskiarvo: {keskiarvo: .2f}")