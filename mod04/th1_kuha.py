##Kysy kuhan pituutta
kuha = float(input("Anna on kuhan pituus senttimetreinä: "))

##Jos alle 37cm, laske takaisin järveen ja montako senttiä alimmasta sallitusta pyyntimitasta puuttuu
sallittu = 37
if kuha < 37:
    print(f"Kuha on liian pieni - laske se takaisin järveen. Kuhan pitäisi olla", (sallittu - kuha), "senttimetriä pidempi.")