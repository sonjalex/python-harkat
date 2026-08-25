##Juomat: kahvia, viiniä, olutta, öljyä
##Kaikki voivat tilata kahvia
##Vähintään 18 vuotiaat ihmiset voivat tilata viiniä
##Vähintään 100 vuotiaat tontut voivat tilata olutta
##Kaikki robotit voivat tilata öljyä
##Kysy ikä ja laji, tulosta lista juomista mitä käyttäjä voi tilata

ikä = int(input("Minkä ikäinen olet? "))
laji = str(input("Mikä lajisi on? "))

if laji == "robotti":
    print("Kahvi, öljy")
elif laji == "ihminen" and ikä >= 18:
    print("Kahvi, viini")
elif laji == "ihminen" and ikä < 18:
    print("Kahvi")
elif laji == "tonttu" and ikä >= 100:
    print("Kahvi, olut")
elif laji == "tonttu" and ikä < 100:
    print("Kahvi")