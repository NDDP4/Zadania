from collections import namedtuple


Punkt = namedtuple("Punkt", ["x", "y"])


def wczytaj_punkty():
    n = int(input("Podaj liczbę punktów: "))
    punkty = []
    for i in range(n):
        x, y = map(int, input(f"Podaj punkt {i + 1} (x y): ").split())
        punkty.append(Punkt(x, y))

    return punkty


def odleglosc_kwadratowa(p1, p2):
    return (p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2


def znajdz_najdalsza_pare(punkty):
    max_odleglosc = -1
    para = None
    for i in range(len(punkty)):
        for j in range(i + 1, len(punkty)):
            d = odleglosc_kwadratowa(punkty[i], punkty[j])
            if d > max_odleglosc:
                max_odleglosc = d
                para = (punkty[i], punkty[j])
    odleglosc = max_odleglosc ** 0.5

    return para, odleglosc


def policz_pierwsza_cwiartke(punkty):
    licznik = 0
    for punkt in punkty:
        if punkt.x > 0 and punkt.y > 0:
            licznik += 1

    return licznik


def znajdz_trojkaty_rownoboczne(punkty):
    trojkaty = []
    for i in range(len(punkty)):
        for j in range(i + 1, len(punkty)):
            for k in range(j + 1, len(punkty)):
                d1 = odleglosc_kwadratowa(punkty[i], punkty[j])
                d2 = odleglosc_kwadratowa(punkty[i], punkty[k])
                d3 = odleglosc_kwadratowa(punkty[j], punkty[k])
                if d1 == d2 == d3 and d1 > 0:
                    trojkaty.append(
                        (punkty[i], punkty[j], punkty[k])
                    )

    return trojkaty


def wyswietl_wyniki(punkty):
    print("\na. Najdalsza para punktów ")
    para, odleglosc = znajdz_najdalsza_pare(punkty)

    print("Punkty:", para[0], "i", para[1])
    print("Odległość:", round(odleglosc, 2))

    print("\nb. Pierwsza ćwiartka")

    liczba = policz_pierwsza_cwiartke(punkty)
    print("Liczba punktów:", liczba)

    print("\nc. Trójkąty równoboczne")
    trojkaty = znajdz_trojkaty_rownoboczne(punkty)

    if len(trojkaty) == 0:
        print("Nie znaleziono trójkątów równobocznych.")
    else:
        for trojkat in trojkaty:
            print(trojkat)


def main():
    punkty = wczytaj_punkty()
    wyswietl_wyniki(punkty)


if __name__ == "__main__":
    main()