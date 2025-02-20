def najdluzszy_ciag_niemalejacy(nazwa_pliku):
    try:
        with open(nazwa_pliku, 'r') as plik:
            liczby = [float(linia.strip()) for linia in plik if linia.strip()]

        if not liczby:
            return None, 0

        najdluzszy_ciag = []
        aktualny_ciag = [liczby[0]]

        for i in range(1, len(liczby)):
            if liczby[i] >= liczby[i - 1]:
                aktualny_ciag.append(liczby[i])
            else:
                if len(aktualny_ciag) > len(najdluzszy_ciag):
                    najdluzszy_ciag = aktualny_ciag
                aktualny_ciag = [liczby[i]]

        if len(aktualny_ciag) > len(najdluzszy_ciag):
            najdluzszy_ciag = aktualny_ciag

        return najdluzszy_ciag[0], len(najdluzszy_ciag)

    except Exception as e:
        print(f"Błąd: {e}")
        return None, 0

plik_nazwa = "dane.txt"
pierwszy_element, dlugosc_ciagu = najdluzszy_ciag_niemalejacy(plik_nazwa)

if pierwszy_element is not None:
    print(f"Pierwszy element ciągu: {pierwszy_element}")
    print(f"Liczba elementów: {dlugosc_ciagu}")
else:
    print("Brak danych lub błąd odczytu.")