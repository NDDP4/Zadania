import math
def pobieranie_liczb():
    while True:
        try:
            return int(input("Pobieranie: "))
        except ValueError:
            print("Podaj liczbę!")


def cyfry_parzyste(n):
    ile = 0
    for cyfra in str(abs(n)):
        if int(cyfra) % 2 == 0:
            ile += 1
    return ile

def cyfry_nieparzyste(n):
    ile = 0
    for cyfra in str(abs(n)):
        if int(cyfra) % 2 != 0:
            ile += 1
    return ile


def liczba_dzielnikow(n):
    n = abs(n)

    if n == 0:
        return 0

    ile = 0
    i = 1
    while i * i <= n:
        if n % i == 0:
            if i == n // i:
                ile += 1
            else:
                ile += 2
        i += 1
    return ile

def odchylenie_standardowe(a, b):
    srednia = (a + b) / 2
    return math.sqrt(((a - srednia) ** 2 + (b - srednia) ** 2) / 2)


def main():
    while True:
        a = pobieranie_liczb()
        b = pobieranie_liczb()

        if cyfry_parzyste(a) == cyfry_nieparzyste(b):
            break

    dz_a = liczba_dzielnikow(a)
    dz_b = liczba_dzielnikow(b)

    if dz_a > dz_b:
        print(a)
    elif dz_b > dz_a:
        print(b)
    else:
        print(odchylenie_standardowe(a, b))


if __name__ == "__main__":
    main()
