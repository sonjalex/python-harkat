def parilliset(luvut):
    luvut.sort()
    for pariton in range(len(luvut) - 1, -1, -1):
        luku = luvut[pariton]
        if luku % 2 != 0:
            lista.remove(int(luku))
    return lista

lista = []

luku = input("Syötä kokonaisluku (tyhjä lopettaa): ")

while luku != "":
    lista.append(int(luku))
    luku = input("Syötä kokonaisluku (tyhjä lopettaa): ")

print("Parillisia lukuja ovat: ", parilliset(lista))