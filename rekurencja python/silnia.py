def silnia(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * silnia(n - 1)

# Przykład użycia
n = 5
wynik = silnia(n)
print(f"Silnia z {n} wynosi: {wynik}")
