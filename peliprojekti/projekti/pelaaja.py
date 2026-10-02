class Pelaaja:
    def __init__(self, nimi, ikä):
        self.nimi = nimi
        self.ikä = ikä

    def nimi():
        pelaajan_nimi = input("Syötä pelaajan nimi: ")
        print(f"\nHei {pelaajan_nimi} tervetuloa!")

    def ikä():
        ikä = int(input("Syötä pelaajan ikä: "))
        if ikä >= 12:
            print(f"Ikäsi on {ikä}.")
        else:
            print("Olet alaikäinen.")