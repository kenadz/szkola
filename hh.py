def najdluzszy_ciag_niemalejacy(nazwa_pliku):
    try:
        with open(nazwa_pliku, 'r') as plik:
            liczby = [float(linia.strip()) for linia in plik if linia.strip()]

        if not liczby:
            return []

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

        return najdluzszy_ciag

    except Exception as e:
        print(f"Błąd: {e}")
        return []

plik_nazwa = "dane.txt"
ciag = najdluzszy_ciag_niemalejacy(plik_nazwa)

if ciag:
    print(f"Najdłuższy niemalejący ciąg: {ciag}")
else:
    print("Brak danych lub błąd odczytu.")