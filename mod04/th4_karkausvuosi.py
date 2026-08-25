vuosi = int(input("Syötä vuosiluku: "))

if vuosi < 100 and vuosi % 4 == 0 or vuosi > 100 and vuosi % 400 == 0 and vuosi % 100 == 0:
    print(f"Vuosi {vuosi} on karkausvuosi.")
else:
    print(f"Vuosi {vuosi} ei ole karkausvuosi.")