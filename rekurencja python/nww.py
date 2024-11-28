def nwd(a, b):
    if b == 0:
        return a
    else:
        return nwd(b, a % b)

def nww(a, b):
    return abs(a * b) // nwd(a, b)

# Przykład użycia
liczba1 = 12
liczba2 = 18
wynik = nww(liczba1, liczba2)
print(f"NWW({liczba1}, {liczba2}) =", wynik)
