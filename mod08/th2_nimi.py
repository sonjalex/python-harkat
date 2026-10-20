nimet = set()

nimi1 = input("Anna nimi: ")

nimet.add(nimi1)
print("Uusi nimi")

nimi2 = input("Anna nimi: ")
if nimi2 == nimi1:
    print("Aiemmin syötetty nimi")
else:
    print("Uusi nimi")

while nimi2 != "":
    nimi2 = input("Anna nimi: ")
    if nimi2 in nimet:
        print("Aiemmin syötetty nimi")
    if nimi2 not in nimet:
        print("Uusi nimi")
    if nimi2 != "":
        print("Uusi nimi")
    nimet.add(nimi2)


for n in nimet:
    print(n)