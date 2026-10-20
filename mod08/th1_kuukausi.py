kuukausi = ("tammikuu", "helmikuu", "maaliskuu", "huhtikuu", "toukokuu", "kesäkuu", "heinäkuu", "elokuu", "syyskuu", "lokakuu", "marraskuu", "joulukuu")

vuodenajat = ("talvi", "talvi", "kevät", "kevät", "kevät", "kesä", "kesä", "kesä", "syksy", "syksy", "syksy", "talvi")

vuodenaika = int(input("Syötä kuukauden numero: "))

# Haetaan kuukauden nimen ja vuodenajan indeksit (numero - 1)
valittu_kuukausi = kuukausi[vuodenaika - 1]
valittu_vuodenaika = vuodenajat[vuodenaika - 1]

# Tulostetaan kuukauden nimi ja sitä vastaava vuodenaika
print(f"{valittu_kuukausi}, {valittu_vuodenaika}")
