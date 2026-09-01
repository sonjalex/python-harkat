##While-seikkailu

ase = input("Maria oli rohkea ritari, joka joutui kaksintaisteluun. Minkä aseen Maria ottaa? ")

while ase != "miekka":
    print("Ei kannata, se on huono ase.")
    ase = input("Anna toinen ase. ")
    if ase == "miekka":
            break
print("Miekalla Maria voittaa varmasti!")