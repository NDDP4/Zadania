

from collections import namedtuple

Pracownik = namedtuple('Pracownik', ['imie', 'nazwisko', 'stanowisko', 'zarobki'])

def wyswietl_pracownikow(lista, komunikat):
    print(f"\n{komunikat}:")
    print("-" * 60)
    for p in lista:
        print(f"{p.imie} {p.nazwisko}, {p.stanowisko}, {p.zarobki} zł")
    print("-" * 60)

def znajdz_po_stanowisku(pracownicy, stanowisko):
    wynik = []
    for p in pracownicy:
        if p.stanowisko == stanowisko:
            wynik.append(p)
    return wynik

def znajdz_w_przedziale(pracownicy, min_zarobki, max_zarobki):
    wynik = []
    for p in pracownicy:
        if min_zarobki <= p.zarobki <= max_zarobki:
            wynik.append(p)
    return wynik

def usun_pracownikow(pracownicy, stanowisko, prog_zarobkow):
    wynik = []
    for p in pracownicy:
        if not (p.stanowisko == stanowisko and p.zarobki > prog_zarobkow):
            wynik.append(p)
    return wynik

def przyznaj_podwyzke(pracownicy, stanowisko, procent):
    wynik = []
    for p in pracownicy:
        if p.stanowisko == stanowisko:
            nowe_zarobki = p.zarobki * (1 + procent / 100)
            nowy_pracownik = p._replace(zarobki=round(nowe_zarobki, 2))
            wynik.append(nowy_pracownik)
        else:
            wynik.append(p)
    return wynik

def main():

    pracownicy = [
        Pracownik("Anna", "Kowalska", "Programista", 8500),
        Pracownik("Jan", "Nowak", "Programista", 7200),
        Pracownik("Maria", "Wiśniewska", "Analityk", 6400),
        Pracownik("Piotr", "Wójcik", "Programista", 9800),
        Pracownik("Katarzyna", "Kamińska", "Manager", 12000),
        Pracownik("Tomasz", "Lewandowski", "Analityk", 5800),
        Pracownik("Agnieszka", "Zielińska", "Programista", 6700),
        Pracownik("Michał", "Szymański", "Tester", 5500)
    ]

    wyswietl_pracownikow(pracownicy, "Wszyscy pracownicy")

    programisci = znajdz_po_stanowisku(pracownicy, "Programista")
    wyswietl_pracownikow(programisci, "Programiści")

    przedzial_zarobkow = znajdz_w_przedziale(pracownicy, 6000, 8000)
    wyswietl_pracownikow(przedzial_zarobkow, "Pracownicy z zarobkami 6000-8000 zł")

    pracownicy_po_usunieciu = usun_pracownikow(pracownicy, "Programista", 8000)
    wyswietl_pracownikow(pracownicy_po_usunieciu, "Po usunięciu programistów zarabiających > 8000 zł")

    pracownicy_po_podwyzce = przyznaj_podwyzke(pracownicy_po_usunieciu, "Analityk", 10)
    wyswietl_pracownikow(pracownicy_po_podwyzce, "Po 10% podwyżce dla analityków")
    
    print(f"\nPodsumowanie:")
    print(f"Początkowa liczba pracowników: {len(pracownicy)}")
    print(f"Liczba po usunięciu: {len(pracownicy_po_usunieciu)}")
    print(f"Liczba po podwyżce: {len(pracownicy_po_podwyzce)}")

if __name__ == "__main__":
    main()
