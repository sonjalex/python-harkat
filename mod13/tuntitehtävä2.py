while True:
    try:
        luku1 = int(input("Anna luku: "))
        luku2 = int(input("Anna luku: "))
        jakolasku = luku1 / luku2
        print(f"{jakolasku}")

    except ValueError:
        print(f"Virhe, jakolaskun pitää olla numero")

    except ZeroDivisionError:
        print(f"Virhe, ei voi jakaa nollalla")