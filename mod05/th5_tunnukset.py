## käyttäjätunnus = python
## salasana = rules

tunnus = input("Syötä käyttäjätunnus: ")
salasana = input("Syötä salasana: ")
yritykset = 1

while yritykset < 5:
    if tunnus == "python" and salasana == "rules":
        print("Tervetuloa.")
        yritykset = 5
    else:
        tunnus = input("Syötä käyttäjätunnus: ")
        salasana = input("Syötä salasana: ")
        yritykset += 1
        if yritykset == 5:
            print("Pääsy evätty.")