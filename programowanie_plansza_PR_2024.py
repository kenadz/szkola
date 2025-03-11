def wczytaj_plansze(nazwa_pliku):
    plansza = []
    with open(nazwa_pliku, 'r') as plik:
        for _ in plik:
            wiersz = [int(i) for i in _.strip().split()]
            plansza.append(wiersz)
    return plansza

def czy_mozna_umiescic_jednomasztowiec(plansza, wiersz, kolumna):
    """Sprawdź czy pozycja jest odpowiednia dla umieszczenia jednomasztowca."""
    # czy komórka pusta (0)
    if plansza[wiersz][kolumna] != 0:
        return False
    
    # sprawdza sąsiednie komórki (boki i ukośne)
    wiersze, kolumny = len(plansza), len(plansza[0])
    for dw in [-1, 0, 1]:
        for dk in [-1, 0, 1]:
            if dw == 0 and dk == 0:
                continue  # pomija tą samą komórkę
            
            nw, nk = wiersz + dw, kolumna + dk
            if 0 <= nw < wiersze and 0 <= nk < kolumny and plansza[nw][nk] == 1:
                return False  # sąsiad z innym statkiem - X
    
    return True

def licz_mozliwe_pozycje(plansza):
    """Czy jednomasztowiec"""
    wiersze, kolumny = len(plansza), len(plansza[0])
    licznik = 0
    
    for w in range(wiersze):
        for k in range(kolumny):
            if czy_mozna_umiescic_jednomasztowiec(plansza, w, k):
                licznik += 1
    
    return licznik

def licz_symetryczne_pary_jednomasztowcow(plansza):
    """Para jednomasztowców względem przekątnej"""
    wiersze, kolumny = len(plansza), len(plansza[0])
    licznik = 0
    
    for w in range(wiersze):
        for k in range(kolumny):
            # czy jednomasztowiec na (w, k)
            if plansza[w][k] == 1:
                # czy jednomasztowiec (bez sąsiadów)
                jest_jednomasztowcem = True
                for dw, dk in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    nw, nk = w + dw, k + dk
                    if 0 <= nw < wiersze and 0 <= nk < kolumny and plansza[nw][nk] == 1:
                        jest_jednomasztowcem = False
                        break
                
                if jest_jednomasztowcem:
                    # czy symetryczną pozycję (k, w)
                    if k < wiersze and w < kolumny and k != w and plansza[k][w] == 1:
                        # czy symetryczna pozycja jest jednomasztowcem
                        sym_jest_jednomasztowcem = True
                        for dw, dk in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                            nw, nk = k + dw, w + dk
                            if 0 <= nw < wiersze and 0 <= nk < kolumny and plansza[nw][nk] == 1:
                                sym_jest_jednomasztowcem = False
                                break
                        
                        if sym_jest_jednomasztowcem:
                            licznik += 1
    
    # para // 2
    return licznik // 2

def licz_dwumasztowce(plansza):
    wiersze, kolumny = len(plansza), len(plansza[0])
    odwiedzone = set()
    licznik = 0
    
    for w in range(wiersze):
        for k in range(kolumny):
            if plansza[w][k] == 1 and (w, k) not in odwiedzone:
                # poziomy sąsiad
                if k + 1 < kolumny and plansza[w][k+1] == 1:
                    licznik += 1
                    odwiedzone.add((w, k))
                    odwiedzone.add((w, k+1))
                # pionowy sąsiad
                elif w + 1 < wiersze and plansza[w+1][k] == 1:
                    licznik += 1
                    odwiedzone.add((w, k))
                    odwiedzone.add((w+1, k))
                # brak sąsiadów - jednomasztowiec
                else:
                    odwiedzone.add((w, k))
    
    return licznik

def licz_statki_na_przekatnych(plansza):
    """
    Policz jednomasztowce i dwumasztowce z przynajmniej jedną komórką
    na jednej z głównych przekątnych.
    """
    wiersze, kolumny = len(plansza), len(plansza[0])
    liczba_jednomasztowcow = 0
    liczba_dwumasztowcow = 0
    odwiedzone = set()
    
    # czy główna przekątną (od lewego górnego do prawego dolnego rogu)
    komorki_glownej_przekatnej = {(i, i) for i in range(min(wiersze, kolumny))}
    
    # czy przeciwna przekątną (od prawego górnego do lewego dolnego rogu)
    komorki_przeciwnej_przekatnej = {(i, kolumny-1-i) for i in range(min(wiersze, kolumny))}
    
    # wszystkie komórki przekątnych
    komorki_przekatnych = komorki_glownej_przekatnej.union(komorki_przeciwnej_przekatnej)
    
    for w in range(wiersze):
        for k in range(kolumny):
            if plansza[w][k] == 1 and (w, k) not in odwiedzone:
                # czy dwumasztowiec
                jest_dwumasztowcem = False
                dwumasztowiec_na_przekatnej = False
                
                # poziomy sąsiad
                if k + 1 < kolumny and plansza[w][k+1] == 1:
                    jest_dwumasztowcem = True
                    odwiedzone.add((w, k))
                    odwiedzone.add((w, k+1))
                    if (w, k) in komorki_przekatnych or (w, k+1) in komorki_przekatnych:
                        dwumasztowiec_na_przekatnej = True
                
                # pionowy sąsiad
                elif w + 1 < wiersze and plansza[w+1][k] == 1:
                    jest_dwumasztowcem = True
                    odwiedzone.add((w, k))
                    odwiedzone.add((w+1, k))
                    if (w, k) in komorki_przekatnych or (w+1, k) in komorki_przekatnych:
                        dwumasztowiec_na_przekatnej = True
                
                # brak sąsiadów - jednomasztowiec
                if not jest_dwumasztowcem:
                    odwiedzone.add((w, k))
                    if (w, k) in komorki_przekatnych:
                        liczba_jednomasztowcow += 1
                elif dwumasztowiec_na_przekatnej:
                    liczba_dwumasztowcow += 1
    
    return liczba_jednomasztowcow, liczba_dwumasztowcow

def main():
    plansza = wczytaj_plansze("plansza.txt")
    
    with open("wynik4.txt", "w") as wyjscie:
        mozliwe_pozycje = licz_mozliwe_pozycje(plansza)
        wyjscie.write("4.1.\n")
        wyjscie.write(f"{mozliwe_pozycje}\n\n")
        
        pary_symetryczne = licz_symetryczne_pary_jednomasztowcow(plansza)
        wyjscie.write("4.2.\n")
        wyjscie.write(f"{pary_symetryczne}\n\n")
        
        dwumasztowce = licz_dwumasztowce(plansza)
        wyjscie.write("4.3.\n")
        wyjscie.write(f"{dwumasztowce}\n\n")
        
        jednomasztowce_na_przekatnej, dwumasztowce_na_przekatnej = licz_statki_na_przekatnych(plansza)
        wyjscie.write("4.4.\n")
        wyjscie.write(f"{jednomasztowce_na_przekatnej}\n")
        wyjscie.write(f"{dwumasztowce_na_przekatnej}\n")

if __name__ == "__main__":
    main()
