def summa(luvut):
    summa = 0
    for luku in luvut:
        summa += luku
    return summa

lista = []

luku = input("Syötä kokonaisluku (tyhjä lopettaa): ")

while luku != "":
    lista.append(int(luku))
    luku = input("Syötä kokonaisluku (tyhjä lopettaa): ")

tulos = summa(lista)
print(f"Summa on: {tulos}")