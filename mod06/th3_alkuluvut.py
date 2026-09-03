luku = int(input("Syötä luku: "))

alkuluku = "On alkuluku"

for x in range(2, int(luku**0.5) + 1):
    if luku % x == 0:
        alkuluku = "Ei ole alkuluku"
        break
print(alkuluku)