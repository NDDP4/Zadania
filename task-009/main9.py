# Numer analyzer
# Funkcja pobiera od usera liczbe naturalna i konczy kiedy bedzie w zakresie [a, b].
# Kolejna funkcja przyjmuje te liczbe i jako drugi argument dostaje Callable, ktore
# ma wykonac operacje na tej liczbie:
# a. Zwraca sume cyfr.
# b. Zwraca najwieksza cyfre.
# c. Zwraca ilosc unikalnych cyfr (jak juz umiesz liste) 


from typing import Callable


def pobierz_liczbe(x: int, y: int) -> int:
    while True:
        a = int(input(f"Wybierz liczbę z zakresu od {x} do {y}: "))

        if x <= a <= y:
            return a

        print(f"Liczba musi być w zakresie od {x} do {y}].")


def wykonaj_operacje(a: int, operacja: Callable[[int], int]) -> int:
    return operacja(a)


def suma_cyfr(a: int) -> int:
    suma = 0

    while a > 0:
        suma += a % 10
        a //= 10
    return suma


def najwieksza_cyfra(a: int) -> int:
    najwieksza = 0

    while a > 0:
        cyfra = a % 10
        if cyfra > najwieksza:
            najwieksza = cyfra
        a //= 10

    return najwieksza


def ilosc_unikalnych_cyfr(a: int) -> int:
    cyfry = []

    while a > 0:
        cyfra = a % 10
        if cyfra not in cyfry:
            cyfry.append(cyfra)
        a //= 10

    return len(cyfry)


def main() -> None:
    a = pobierz_liczbe(100, 999)

    print("\nWybierz operację:")
    print("1 - Suma cyfr")
    print("2 - Największa cyfra")
    print("3 - Ilość unikalnych cyfr")

    option = int(input("Wybierz opcję: "))

    match option:
        case 1:
            print("Wynik:", wykonaj_operacje(a, suma_cyfr))
        case 2:
            print("Wynik:", wykonaj_operacje(a, najwieksza_cyfra))
        case 3:
            print("Wynik:", wykonaj_operacje(a, ilosc_unikalnych_cyfr))
        case _:
            print("Nie ma takiej opcji")

if __name__ == "__main__":
    main()