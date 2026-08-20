


def przetworz_pary(pary: list[tuple[int, int]]) -> tuple[list[int], int, int]:
    nowa_lista: list[int] = []
    
    for para in pary:
        a, b = para
        
        a_jednosci = a % 10
        a_dziesiatek = a // 10
        b_jednosci = b % 10
        b_dziesiatek = b // 10
        
        U = max(a_jednosci, b_jednosci)
        
        D = min(a_dziesiatek, b_dziesiatek)
        
        nowa_liczba = U * 10 + D
        nowa_lista.append(nowa_liczba)
    
    najwieksza = max(nowa_lista)
    najmniejsza = min(nowa_lista)
    
    return nowa_lista, najwieksza, najmniejsza

pary: list[tuple[int, int]] = [
    (12, 35),
    (31, 22),
    (34, 56)
]

nowa_lista, najwieksza, najmniejsza = przetworz_pary(pary)

print(f"Nowa lista: {nowa_lista}")
print(f"Największa liczba: {najwieksza}")
print(f"Najmniejsza liczba: {najmniejsza}")