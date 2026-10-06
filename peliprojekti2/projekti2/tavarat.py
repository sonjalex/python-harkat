import random

reppu = []

def tavarat():
        lisätäänkö = input("Haluatko lisätä reppuusi jotain matkaa varten? Pitää muistaa ettei metsässä välttämättä ole toimivaa nettiyhteyttä ja matka olisi muutenkin kivempi taittaa ilman puhelinta! Vastaa 'kyllä' tai 'ei'" )

        if lisätäänkö != "kyllä" and lisätäänkö != "ei":
            lisätäänkö = input("\nVastaa 'kyllä' tai 'ei' ")

        if lisätäänkö == "ei":
            print("\nOletko nyt ihan varma? Jos lisättäisiin jotain kuitenkin..")
            joo_tai_ei = input("Vastaa 'lisätään' tai 'ei'")
            if joo_tai_ei == "lisätään":
                print("Tuo on varmasti parempi valinta!")
            if joo_tai_ei == "ei":
                print("Selvä sitten!")

        if lisätäänkö == "kyllä" or joo_tai_ei == "lisätään":
            mukaan = input("\nMitä haluat lisätä reppuusi? ")
            reppu.append(mukaan)
            if mukaan == "":
                if "" in reppu:
                    reppu.remove("")
            while mukaan != "":
                print(f"{mukaan} on lisätty reppuusi")
                mukaan = input("")
                if mukaan == "":
                    if "" in reppu:
                        reppu.remove("")
                mukaan = input("\nMitä haluat lisätä reppuusi? ")
                reppu.append(mukaan)
        while mukaan == "":
                if reppu != "kartta":
                    print("\nHaluaisit olla matkan ilman puhelintasi, eikä netti välttämättä toimi metsässä - haluatko ottaa alueen kartan mukaasi?")
                    vastaus = input("Kyllä vai ei?" )
                    kerrat = 0
                    while vastaus != "kyllä" or vastaus != "ei" and kerrat <= 3:
                        if kerrat == 4 and vastaus != ("kyllä" or "ei"):
                            print("No ei väkisin!")
                            break
                        if vastaus == "kyllä":
                            print("Hyvä, nyt et ainakaan eksy, jos polut eivät näytäkkään tutuilta!")
                            reppu.append("kartta")
                            print(f"Kartta on lisätty reppuusi")
                            break
                        if vastaus == "ei":
                            print("Muistat varmasti reitin yhtä hyvin kuin oman nimesi - eihän karttaa tarvitse mihinkään!")
                            break
                        kerrat += 1
                        numero = random.randint(1,3)
                        if numero == 1:
                            vastaus = input("Ei tuo ollut kysymys :( Syötä kyllä tai ei: ")
                        elif numero == 2:
                            vastaus = input("Uskon, että osaat keskittyä sen verran että vastaat 'kyllä' tai 'ei': ")
                        elif numero == 3:
                            vastaus = input("Lueppa vähän tarkemmin: 'Syötä kyllä tai ei': ")
                if reppu != "kasvikirja":
                    print("\nHuomaat sivusilmällä kirjan kasveista, tahtoisit olla matkan ilman puhelintasi eikä netti välttämättä toimi -  haluatko ottaa kirjan mukaan?")
                    vastaus = input("Kyllä vai ei?")
                    kerrat = 0
                    while vastaus != "kyllä" or vastaus != "ei" and kerrat <= 3:
                        if kerrat == 4 and vastaus != ("kyllä" or "ei"):
                            print("No ei väkisin!")
                            break
                        if vastaus == "kyllä":
                            print("Hyvä, kasvikirja kannattaa olla mukana, jotta tunnistat ovatko kasvit myrkyllisiä!")
                            reppu.append("kasvikirja")
                            print("Kasvikirja on lisätty reppuusi")
                            break
                        if vastaus == "ei":
                            print("No... jos olet ihan varma!")
                            break
                        kerrat += 1
                        numero = random.randint(1,3)
                        if numero == 1:
                            vastaus = input("Ei tuo ollut kysymys :( Syötä kyllä tai ei: ")
                        elif numero == 2:
                            vastaus = input("Uskon, että osaat keskittyä sen verran että vastaat 'kyllä' tai 'ei': ")
                        elif numero == 3:
                            vastaus = input("Lueppa vähän tarkemmin: 'Syötä kyllä tai ei': ")
                if reppu != "vettä" or "vesipullo" or "vesi":
                    print("\nPidemmälle matkalle olisi varmaan hyvä ottaa jotain juotavaa mukaan, eikö totta?")
                    vastaus = input("Kyllä vai ei?")
                    kerrat = 0
                    while vastaus != "kyllä" or vastaus != "ei" and kerrat <= 3:
                        if kerrat == 4 and vastaus != ("kyllä" or "ei"):
                            print("No ei väkisin!")
                            break
                        if vastaus == "kyllä":
                            print("Lisäät vesipullon reppuusi - ihan fiksu päätös.")
                            reppu.append("vesipullo")
                            print("Vesipullo on lisätty reppuusi")
                            break
                        if vastaus == "ei":
                            print("No ei sitä vettä ennenkään ole tarvinnut!")
                            break
                        kerrat += 1
                        numero = random.randint(1,3)
                        if numero == 1:
                            vastaus = input("Ei tuo ollut kysymys :( Syötä kyllä tai ei: ")
                        elif numero == 2:
                            vastaus = input("Uskon, että osaat keskittyä sen verran että vastaat 'kyllä' tai 'ei': ")
                        elif numero == 3:
                            vastaus = input("Lueppa vähän tarkemmin: 'Syötä kyllä tai ei': ")
                break
            

        if any(reppu):
            print("\nRepussassi on")
            for tavara in reppu:
                print("-", tavara)
            print("Vaikuttaa hyvältä, olet valmis retkellesi!")

        if not reppu:
            print("\nReppusi on tyhjä :(")

tavarat()