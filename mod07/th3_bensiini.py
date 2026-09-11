galloonat = int(input("Syötä galloonamäärä joka muunnetaan litroiksi (negatiivinen lopettaa): "))

def litrat():
    litra = galloonat * 3.758
    print(litra)


while galloonat >= 0:
    litrat()
    galloonat = int(input("Syötä galloonamäärä joka muunnetaan litroiksi (negatiivinen lopettaa): "))
else:
    print("Toiminto lopetettu")