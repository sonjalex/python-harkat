cm = float(input("Anna senttimetrit: "))

tuuma = (cm * 2,54)
while tuuma >= 0:
    print(f"{tuuma}")
    cm = float(input("Anna senttimetrit: "))
print("Luku on negatiivinen")