def znajdz_min_max(nazwa_pliku):
    try:
        with open(nazwa_pliku, 'r') as plik:
            liczby = [float(liczba) for linia in plik for liczba in linia.replace(',', ' ').split()]
        
        if not liczby:
            return None, None

        # Ręczne znalezienie min i max
        min_liczba = liczby[0]
        max_liczba = liczby[0]

        for liczba in liczby[1:]:
            if liczba < min_liczba:
                min_liczba = liczba
            if liczba > max_liczba:
                max_liczba = liczba

        return min_liczba, max_liczba
    except Exception as e:
        print(f"Błąd: {e}")
        return None, None

# Przykład użycia
plik_nazwa = "dane.txt"  # Zmień na rzeczywistą nazwę pliku
min_liczba, max_liczba = znajdz_min_max(plik_nazwa)

if min_liczba is not None and max_liczba is not None:
    print(f"Najmniejsza liczba: {min_liczba}")
    print(f"Największa liczba: {max_liczba}")
else:
    print("Brak danych lub błąd odczytu.")