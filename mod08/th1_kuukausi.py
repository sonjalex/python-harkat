# Kevät = maaliskuu, huhtikuu, toukokuu
# Kesä = kesäkuu, heinäkuu, elokuu
# Syksy = syyskuu, lokakuu, marraskuu
# Talvi = joulukuu, tammikuu, helmikuu

kuukausi = ("tammikuu", "helmikuu", "maaliskuu", "huhtikuu", "toukokuu", "kesäkuu", "heinäkuu", "elokuu", "syyskuu", "lokakuu", "marraskuu", "joulukuu")

() = kuukausi

vuodenaika = int(input("Syötä kuukauden numero: "))

vuodenajat = kuukausi[vuodenaika - 1]

print(f"{kuukausi}, {vuodenaika}")