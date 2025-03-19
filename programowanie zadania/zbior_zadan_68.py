def czy_anagramy(a, b):
    return sorted(a) == sorted(b)

def czy_jednolity(napis):
    return all(c == napis[0] for c in napis)

def zadanie_68_1(pary_napisow):
    liczba_wierszy = 0
    for a, b in pary_napisow:
        if czy_jednolity(a) and czy_jednolity(b) and a == b:
            liczba_wierszy += 1
    return liczba_wierszy

def zadanie_68_2(pary_napisow):
    liczba_wierszy = 0
    for a, b in pary_napisow:
        if czy_anagramy(a, b):
            liczba_wierszy += 1
    return liczba_wierszy

def zadanie_68_3(pary_napisow):
    wszystkie_napisy = [napis for para in pary_napisow for napis in para]
    
    grupy = {}
    for napis in wszystkie_napisy:
        posortowany = ''.join(sorted(napis))
        if posortowany not in grupy:
            grupy[posortowany] = []
        grupy[posortowany].append(napis)
    
    max_k = max(len(grupa) for grupa in grupy.values())
    return max_k

with open("dane_napisy.txt", "r") as file:
    pary_napisow = [line.strip().split() for line in file]

wynik_68_1 = zadanie_68_1(pary_napisow)
wynik_68_2 = zadanie_68_2(pary_napisow)
wynik_68_3 = zadanie_68_3(pary_napisow)

with open("wyniki_anagramy.txt", "w") as file:
    file.write(f"68.1\n{wynik_68_1}\n")
    file.write(f"68.2\n{wynik_68_2}\n")
    file.write(f"68.3\n{wynik_68_3}\n")
