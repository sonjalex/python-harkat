import random

nopat = int(input("Kerro arpakuutioiden määrä: "))
summa = 0

for luvut in range(nopat):
    noppa = random.randint(1,6)
    summa += noppa

print(f"Silmälukujen summa on {summa}")