def zmiana_na_dziesietny(liczba, podstawa_poczatek):
    """Konwertuje liczbę z dowolnego systemu na dziesiętny."""
    wartosc_dziesietna = 0
    dlugosc = len(liczba)
    
    for i in range(dlugosc):
        cyfra = liczba[dlugosc - 1 - i]  # Iterowanie od końca
        if '0' <= cyfra <= '9':
            wartosc_cyfry = int(cyfra)
        else:
            wartosc_cyfry = ord(cyfra.upper()) - ord('A') + 10
        wartosc_dziesietna += wartosc_cyfry * (podstawa_poczatek ** i)
    return wartosc_dziesietna

def zmiana_z_dziesietnego(wartosc_dziesietna, podstawa_koniec):
    if wartosc_dziesietna == 0:
        return "0"
    
    wynik = ""
    while wartosc_dziesietna > 0:
        reszta = wartosc_dziesietna % podstawa_koniec
        if reszta < 10:
            wynik += str(reszta)
        else:
            wynik += chr(ord('A') + reszta - 10)
        wartosc_dziesietna //= podstawa_koniec

    wynik_odwrocony = ""
    for i in range(len(wynik) - 1, -1, -1):
        wynik_odwrocony += wynik[i]
    return wynik_odwrocony

def main():
    liczba = input("Podaj liczbe: ")
    podstawa_poczatek = int(input("Podaj podstawe systemu zrodlowego: "))
    podstawa_koniec = int(input("Podaj podstawe systemu docelowego: "))

    wartosc_dziesietna = zmiana_na_dziesietny(liczba, podstawa_poczatek)

    wynik = zmiana_z_dziesietnego(wartosc_dziesietna, podstawa_koniec)
    
    print(f"Liczba w systemie docelowym: {wynik}")

main()
