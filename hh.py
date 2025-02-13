def zadanie_60_3(liczby):
    posortowane = sorted(liczby, reverse=True)  # Sortujemy malejąco

    for liczba in posortowane:
        względnie_pierwsza = True  # Zakładamy, że liczba spełnia warunek

        for inna in liczby:
            if liczba != inna and nwd(liczba, inna) != 1:  # Sprawdzamy NWD
                względnie_pierwsza = False
                break  # Nie ma sensu sprawdzać dalej, liczba odpada

        if względnie_pierwsza:
            return liczba  # Znaleźliśmy liczbę spełniającą warunek

    return None  # Jeśli nie znaleźliśmy żadnej, zwracamy None