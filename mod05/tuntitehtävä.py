vuosi = int(input("Anna vuosiluku: "))

while vuosi >= 1896:

    if vuosi % 4 == 0:
        print("Vuosi on olympiavuosi")
    else:
        print("Vuosi ei ole olympiavuosi")

    vuosi = int(input("Anna vuosiluku: "))

print("Ohjelma on ohi")

