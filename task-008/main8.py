from typing import Callable


def czy_liczba_pierwsza(n: int) -> bool:
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


def czy_palindrom(n: int) -> bool:
    oryginalna = n
    odwrocona = 0

    while n > 0:
        cyfra = n % 10
        odwrocona = odwrocona * 10 + cyfra
        n //= 10

    return oryginalna == odwrocona


def czy_doskonala(n: int) -> bool:
    if n <= 1:
        return False

    suma = 1

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            suma += i

            if i != n // i:
                suma += n // i

    return suma == n


def czy_wielokrotnosc_7(n: int) -> bool:
    return n % 7 == 0


def wybierz_funkcje(wybor: int) -> Callable[[int], bool]:
    match wybor:
        case 1:
            return czy_liczba_pierwsza
        case 2:
            return czy_palindrom
        case 3:
            return czy_doskonala
        case 4:
            return czy_wielokrotnosc_7
        case _:
            raise ValueError("Nieprawidłowy wybór.")


def znajdz_liczbe(funkcja: Callable[[int], bool]) -> int:
    while True:
        liczba = int(input("Podaj liczbę: "))

        if liczba < 0:
            raise ValueError("Podano liczbę ujemną.")

        if funkcja(liczba):
            return liczba
        else:
            print("Ta liczba nie spełnia warunku funkcji.")


def main() -> None:
    print("Wybierz właściwość liczby:")
    print("1 - liczba pierwsza")
    print("2 - palindrom")
    print("3 - liczba doskonała")
    print("4 - wielokrotność 7")

    wybor = int(input("Podaj numer (1-4): "))

    wybrana_funkcja = wybierz_funkcje(wybor)

    wynik = znajdz_liczbe(wybrana_funkcja)

    print(f"Znaleziono liczbę:", wynik)


if __name__ == "__main__":
    main()