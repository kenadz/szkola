def wczytaj_liczby(plik):
    with open(plik, "r") as f:
        return [int(line.strip()) for line in f]

def czynniki_pierwsze(n):
    i = 2
    czynniki = []
    while i * i <= n:
        while n % i == 0:
            czynniki.append(i)
            n //= i
        i += 1
    if n > 1:
        czynniki.append(n)
    return czynniki

def zadanie_59_1(liczby):
    count = 0
    for liczba in liczby:
        czynniki = czynniki_pierwsze(liczba)
        unikalne = set(czynniki)
        if len(unikalne) == 3 and all(x % 2 != 0 for x in unikalne):
            count += 1
    return count

def czy_palindrom(n):
    return str(n) == str(n)[::-1]

def zadanie_59_2(liczby):
    count = 0
    for liczba in liczby:
        odwrocona = int(str(liczba)[::-1])
        if czy_palindrom(liczba + odwrocona):
            count += 1
    return count

def iloczyn_cyfr(n):
    wynik = 1
    for cyfra in str(n):
        wynik *= int(cyfra)
    return wynik

def moc_liczby(n):
    k = 0
    while n >= 10:
        n = iloczyn_cyfr(n)
        k += 1
    return k

def zadanie_59_3(liczby):
    moce = {i: 0 for i in range(1, 9)}
    liczby_moc_1 = []
    for liczba in liczby:
        moc = moc_liczby(liczba)
        if moc in moce:
            moce[moc] += 1
        if moc == 1:
            liczby_moc_1.append(liczba)
    
    min_moc_1 = min(liczby_moc_1) if liczby_moc_1 else None
    max_moc_1 = max(liczby_moc_1) if liczby_moc_1 else None
    
    return moce, min_moc_1, max_moc_1

liczby = wczytaj_liczby("liczby.txt")

wynik_59_1 = zadanie_59_1(liczby)
wynik_59_2 = zadanie_59_2(liczby)
wyniki_59_3, min_moc_1, max_moc_1 = zadanie_59_3(liczby)

with open("wyniki_liczby.txt", "w") as f:
    f.write(f"59.1: {wynik_59_1}\n")
    f.write(f"59.2: {wynik_59_2}\n")
    f.write("59.3:\n")
    for moc, liczba in wyniki_59_3.items():
        f.write(f"Moc {moc}: {liczba}\n")
    f.write(f"Min moc 1: {min_moc_1}\n")
    f.write(f"Max moc 1: {max_moc_1}\n")
