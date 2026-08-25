sukupuoli = str(input("Mikä on biologinen sukupuolesi? "))
arvo = float(input("Mikä on hemoglobiiniarvosi? "))

if sukupuoli == "nainen" and 117 <= arvo < 176:
    print("Hemoglobiiniarvosi on normaali.")
elif sukupuoli == "nainen" and arvo < 117:
    print("Hemoglobiiniarvosi on alhainen.")
elif sukupuoli == "nainen" and arvo >= 176:
    print("Hemoglobiiniarvosi on korkea.")
elif sukupuoli == "mies" and 134 <= arvo < 196:
    print("Hemoglobiiniarvosi on normaali.")
elif sukupuoli == "mies" and arvo < 134:
    print("Hemoglobiiniarvosi on alhainen.")
elif sukupuoli == "mies" and arvo > 196:
    print("Hemoglobiiniarvosi on korkea.")
else:
    print("Kirjoitithan sukupuolesi pienellä?")