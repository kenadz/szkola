import math

# Funkcja do wczytania liczb z pliku
def wczytaj_liczby(nazwa_pliku):
    with open(nazwa_pliku, "r") as f:
        return [int(line.strip()) for line in f]

# Funkcja do znajdowania wszystkich dzielników liczby
def znajdz_dzielniki(n):
    dzielniki = set()
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            dzielniki.add(i)
            dzielniki.add(n // i)
    return sorted(dzielniki)

# 60.1. Liczenie liczb mniejszych niż 1000
def zadanie_60_1(liczby):
    mniejsze_niz_1000 = [x for x in liczby if x < 1000]
    return len(mniejsze_niz_1000), mniejsze_niz_1000[-2:]

# 60.2. Liczby z dokładnie 18 dzielnikami
def zadanie_60_2(liczby):
    liczby_18_dzielnikow = []
    for liczba in liczby:
        dzielniki = znajdz_dzielniki(liczba)
        if len(dzielniki) == 18:
            liczby_18_dzielnikow.append((liczba, dzielniki))
    return liczby_18_dzielnikow

# 60.3. Największa liczba względnie pierwsza ze wszystkimi innymi
def nwd(a, b):
    while b:
        a, b = b, a % b
    return a

def zadanie_60_3(liczby):
    posortowane = sorted(liczby, reverse=True)  # Sortujemy malejąco
    for liczba in posortowane:
        if all(nwd(liczba, inna) == 1 for inna in liczby if inna != liczba):
            return liczba
    return None

# Główna funkcja programu
def main():
    liczby = wczytaj_liczby("liczby.txt")

    # 60.1
    liczba_mniejszych, ostatnie_dwie = zadanie_60_1(liczby)

    # 60.2
    liczby_18_dzielnikow = zadanie_60_2(liczby)

    # 60.3
    liczba_wzglednie_pierwsza = zadanie_60_3(liczby)

    # Zapis wyników do pliku
    with open("wyniki.txt", "w") as f:
        # Wyniki 60.1
        f.write(f"60.1: Liczb mniejszych niż 1000: {liczba_mniejszych}\n")
        f.write(f"Ostatnie dwie takie liczby: {ostatnie_dwie[0]}, {ostatnie_dwie[1]}\n\n")

        # Wyniki 60.2
        f.write("60.2: Liczby z dokładnie 18 dzielnikami:\n")
        for liczba, dzielniki in liczby_18_dzielnikow:
            f.write(f"{liczba}: {', '.join(map(str, dzielniki))}\n")
        f.write("\n")

        # Wyniki 60.3
        f.write(f"60.3: Największa liczba względnie pierwsza ze wszystkimi innymi: {liczba_wzglednie_pierwsza}\n")

if __name__ == "__main__":
    main()