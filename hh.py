def porownaj_plik_linie(plik1, plik2):
    try:
        with open(plik1, 'r') as p1, open(plik2, 'r') as p2:
            linie1 = [int(linia.strip(), 8) for linia in p1 if linia.strip()]  # Zamiana na dziesiętny
            linie2 = [float(linia.strip()) for linia in p2 if linia.strip()]  # Zakładamy, że liczby w pliku 2 są w dziesiętnym

        min_dlugosc = min(len(linie1), len(linie2))

        licznik_rownych = sum(1 for i in range(min_dlugosc) if linie1[i] == linie2[i])
        licznik_wiekszych = sum(1 for i in range(min_dlugosc) if linie1[i] > linie2[i])

        return licznik_rownych, licznik_wiekszych

    except Exception as e:
        print(f"Błąd: {e}")
        return 0, 0

plik1 = "liczby1.txt"  # Plik z liczbami ósemkowymi
plik2 = "liczby2.txt"  # Plik z liczbami dziesiętnymi
rowne, wieksze = porownaj_plik_linie(plik1, plik2)

print(f"Liczba wierszy, gdzie wartości są takie same: {rowne}")
print(f"Liczba wierszy, gdzie wartość w 'liczby1' jest większa niż w 'liczby2': {wieksze}")