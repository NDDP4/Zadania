
def sprawdz_liczby(a: int, b: int) -> bool:
    temp_a = abs(a)
    temp_b = abs(b)

    liczba_cyfr_a = 0
    liczba_cyfr_b = 0

    if temp_a == 0:
        liczba_cyfr_a = 1
    else:
        while temp_a > 0:
            liczba_cyfr_a += 1
            temp_a //= 10

    if temp_b == 0:
        liczba_cyfr_b = 1
    else:
        while temp_b > 0:
            liczba_cyfr_b += 1
            temp_b //= 10

    if liczba_cyfr_a != liczba_cyfr_b:
        raise ValueError("Liczby mają różną liczbę cyfr.")


    a = abs(a)
    b = abs(b)

    while a > 0 and b > 0:
        cyfra_a = a % 10
        cyfra_b = b % 10

        if abs(cyfra_a - cyfra_b) > 1:
            return False

        a //= 10
        b //= 10

    return True


def pobierz_liczby() -> tuple[int, int]:

    while True:
        try:
            a = int(input("Podaj pierwszą liczbę: "))
            b = int(input("Podaj drugą liczbę: "))
            return a, b

        except ValueError:
            print("To nie jest poprawna liczba całkowita.")


def main():
    a, b = pobierz_liczby()

    try:
        if sprawdz_liczby(a, b):
            print(f"Poprawne pary liczb: a = {a}, b = {b}")
        else:
            print("Liczby nie spełniają warunku.")

    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()