

def sprawdz_liczby(a: int, b: int) -> bool:

    sa = str(a)
    sb = str(b)

    if len(sa) != len(sb):
        raise ValueError("Liczby mają różną liczbę cyfr.")
    for da, db in zip(reversed(sa), reversed(sb)):
        if abs(int(da) - int(db)) > 1:
            return False
    return True

def main():
    while True:
        try:
            a = int(input("Podaj pierwszą liczbę całkowitą: "))
            b = int(input("Podaj drugą liczbę całkowitą: "))
        except ValueError:
            print("To nie jest poprawna liczba całkowita. Spróbuj ponownie.")
            continue
        try:
            if sprawdz_liczby(a, b):
                print(f"Poprawne pary liczb: a = {a}, b = {b}")
                break
            else:
                print("Liczby nie spełniają warunku. Spróbuj ponownie.")
        except ValueError as e:
            print(e)
            continue

if __name__ == "__main__":
    main()