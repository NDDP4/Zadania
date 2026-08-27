from collections import namedtuple


Produkt = namedtuple('Produkt', ['nazwa', 'cena', 'znizka'])


def cena_po_znizce(produkt: Produkt) -> float:
    return produkt.cena * (1 - produkt.znizka)


def stworz_liste_produktow() -> list[Produkt]:  
    return [
        Produkt('Laptop', 4500, 0.15),
        Produkt('Smartfon', 3200, 0.10),
        Produkt('Tablet', 1800, 0.20),
        Produkt('Słuchawki', 450, 0.25),
        Produkt('Monitor', 1500, 0.05),
        Produkt('Klawiatura', 350, 0.15),
        Produkt('Mysz', 150, 0.30),
        Produkt('Drukarka', 1200, 0.12),
    ]


def pogrupuj_produkty(produkty: list[Produkt]) -> dict[float, list[Produkt]]:  
    grupy = {}
    
    for produkt in produkty:
        cena = round(cena_po_znizce(produkt), 2)
        
        if cena not in grupy:
            grupy[cena] = []
        
        grupy[cena].append(produkt)
    
    return grupy


def wyswietl_grupy_produktow(grupy: dict[float, list[Produkt]]) -> None:
    print("PRODUKTY POGUPOWANE WEDŁUG CENY PO ZNIŻCE:")
    print("=" * 60)
    
    for cena in sorted(grupy.keys()):
        print(f"\nCena po zniżce: {cena:.2f} zł")
        print("-" * 40)
        
        for produkt in grupy[cena]:
            cena_po = cena_po_znizce(produkt)
            print(f"  {produkt.nazwa}: {produkt.cena:.2f} zł - {produkt.znizka * 100:.0f}% = {cena_po:.2f} zł")


def znajdz_najdrozsze_produkty(grupy: dict[float, list[Produkt]]) -> tuple[float, list[Produkt]]: 
    if not grupy:
        return 0.0, []
    
    najwyzsza_cena = max(grupy.keys())
    najdrozsze_produkty = grupy[najwyzsza_cena]
    
    return najwyzsza_cena, najdrozsze_produkty


def wyswietl_najdrozsze_produkty(najwyzsza_cena: float, produkty: list[Produkt]) -> None:
    print("\n" + "=" * 60)
    print("PRODUKTY Z NAJWYŻSZĄ CENĄ PO ZNIŻCE:")
    print("=" * 60)
    
    for produkt in produkty:
        cena_po = cena_po_znizce(produkt)
        print(f"\n{produkt.nazwa}")
        print(f"  Cena podstawowa: {produkt.cena:.2f} zł")
        print(f"  Zniżka: {produkt.znizka * 100:.0f}%")
        print(f"  Cena po zniżce: {cena_po:.2f} zł")


def main() -> None:
    produkty = stworz_liste_produktow()
    grupy = pogrupuj_produkty(produkty)
    wyswietl_grupy_produktow(grupy)
    najwyzsza_cena, najdrozsze_produkty = znajdz_najdrozsze_produkty(grupy)
    wyswietl_najdrozsze_produkty(najwyzsza_cena, najdrozsze_produkty)


if __name__ == "__main__":
    main()
