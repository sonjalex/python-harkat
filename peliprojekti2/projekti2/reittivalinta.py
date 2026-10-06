def reittivalinta():
    print("\nSaavut (nimi) metsäreitille. Päivä näyttää kauniilta ja on täydellinen sää pienelle seikkailulle.")
    if "kartta" in tavarat:
        katsotaanko = ("\nEdessäsi on kyltti kahdesta eri reitistä, vasemmalta löytyy (nimi) ja oikealta (nimi).\nMuistat ottaneesi kartan reppuun mukaan, haluatko katsoa karttaa? Vastaa 'kyllä' tai 'ei'")
        if katsotaanko == "kyllä":
            print("\nKaivat kartan repustasi tutkien sitä hetken. Kartan mukaan vasemman polun reitti on helpompi ja oikealle on vaativampi reitti kokeneemmille patikoijille.")
            suunta = input("\nKumpaan suuntaan haluat mennä, vasempaan helpommalle reitille vai oikeaan vaativammalle reitille? 'vasen' vai 'oikea'")
            if suunta == "vasen":
                print("Kävelet kohti (vasenta reittiä), seikkailu voi alkaa!")
            if suunta == "oikea":
                print("Kävelet kohti (oikeaa reittiä), toivottavasti osaat asiasi - seikkailu voi alkaa!")
        if katsotaanko == "ei":
            suunta = input("\nKumpaan suuntaan haluat mennä, vasemmalle reitille vai oikealle reitille? 'vasen' vai 'oikea'")
            if suunta == "vasen":
                print("Kävelet kohti (vasenta reittiä), seikkailu voi alkaa!")
            if suunta == "oikea":
                print("Kävelet kohti (oikeaa reittiä), seikkailu voi alkaa!")
            if suunta != "vasen" or "oikea":
                suunta = input("Valitettavasti sinun pitää valita: 'vasen' vai 'oikea': ")
    if "kartta" not in tavarat:
        suunta = input("\nKumpaan suuntaan haluat mennä, vasemmalle reitille vai oikealle reitille? 'vasen' vai 'oikea'")
        if suunta == "vasen":
            print("Kävelet kohti (vasenta reittiä), seikkailu voi alkaa!")
        if suunta == "oikea":
            print("Kävelet kohti (oikeaa reittiä), seikkailu voi alkaa!")
        if suunta != "vasen" or "oikea":
            suunta = input("Valitettavasti sinun pitää valita: 'vasen' vai 'oikea': ")

def oikea():
    while reittivalinta == oikea:
        print("oikea")

def vasen():
    pass