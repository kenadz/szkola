def czy_wzglednie_pierwsza(liczba, liczby, indeks=0):
    """
    Funkcja sprawdzająca, czy liczba jest względnie pierwsza 
    w stosunku do wszystkich innych liczb w liście.
    """
    if indeks >= len(liczby):  # Jeśli przeszliśmy całą listę, liczba jest względnie pierwsza
        return True  

    inna_liczba = liczby[indeks]

    if liczba != inna_liczba:  # Pomijamy porównanie liczby samej ze sobą
        if nwd(liczba, inna_liczba) != 1:  # Jeśli mają wspólny dzielnik większy niż 1
            return False  

    # Sprawdzamy kolejną liczbę w liście
    return czy_wzglednie_pierwsza(liczba, liczby, indeks + 1)


def znajdz_wzglednie_pierwsza(liczby, indeks=0):
    """
    Rekurencyjna funkcja do znalezienia największej liczby,
    która jest względnie pierwsza ze wszystkimi innymi.
    """
    if indeks >= len(liczby):  # Jeśli przeszliśmy przez całą listę, zwracamy None
        return None  

    liczba = liczby[indeks]  # Pobieramy bieżącą liczbę do sprawdzenia

    if czy_wzglednie_pierwsza(liczba, liczby, 0):  
        return liczba  # Jeśli liczba spełnia warunek, zwracamy ją

    # Przechodzimy do następnej liczby w liście
    return znajdz_wzglednie_pierwsza(liczby, indeks + 1)


def zadanie_60_3(liczby):
    posortowane = sorted(liczby, reverse=True)  # Sortujemy malejąco
    return znajdz_wzglednie_pierwsza(posortowane)  # Uruchamiamy rekurencję


# Algorytm Euklidesa do wyznaczania NWD (rekurencyjnie)
def nwd(a, b):
    if b == 0:
        return a
    return nwd(b, a % b)