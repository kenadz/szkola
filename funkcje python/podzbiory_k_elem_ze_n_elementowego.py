import math

n = int(input("Podaj liczbę elementów zbioru: "))
k = int(input("Podaj liczbę elementów w podzbiorze: "))

# print (math.comb(n, k))

def oblicz_liczbe_podzbiorow(n, k):
    if 0 <= k <= n:
        wynik = 1
        for i in range(min(k, n - k)):
            wynik = wynik * (n - i) // (i + 1)
        return wynik
    else:
        return 0

liczba_podzbiorow = oblicz_liczbe_podzbiorow(n, k)
print("Liczba różnych podzbiorów", k, "-elementowych ze zbioru", n, "-elementowego to:", liczba_podzbiorow)
