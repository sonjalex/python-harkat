pienin = None
suurin = None
luku = 0

luku = input("Anna luku: ")

while luku != "":
    luku = input("Anna luku: ")
    if (luku > suurin):
        suurin = luku
    if (luku < pienin):
        pienin = luku

print (f"Pienin luku on {pienin}, suurin luku on {suurin}")