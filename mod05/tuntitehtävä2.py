summa = 0
parillisten_summa = 0
luku = int(input("Anna luku (negatiivinen luku lopettaa) "))

while luku >= 0:
    summa = summa + luku   
    if luku % 2 == 0:
        parillisten_summa = parillisten_summa + luku
    luku = int(input("Anna luku (negatiivinen luku lopettaa) "))
print("Lukujen summa on:", summa)
print(f"Parillisten lukujen summa on: {parillisten_summa}")