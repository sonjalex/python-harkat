kuukausi = ("tammikuu", "helmikuu", "maaliskuu", "huhtikuu", "toukokuu", "kesäkuu", "heinäkuu", "elokuu", "syyskuu", "lokakuu", "marraskuu", "joulukuu")

vuodenajat = ("talvi", "talvi", "kevät", "kevät", "kevät", "kesä", "kesä", "kesä", "syksy", "syksy", "syksy", "talvi")

vuodenaika = int(input("Syötä kuukauden numero: "))

valittu_kuukausi = kuukausi[vuodenaika - 1]
valittu_vuodenaika = vuodenajat[vuodenaika - 1]

print(f"{valittu_kuukausi}, {valittu_vuodenaika}")
