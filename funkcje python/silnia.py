n = int(input("Podaj liczbę n: "))

def oblicz_silnie(n):
    if n == 0:
        return 1
    else:
        return n * oblicz_silnie(n-1)

silnia = oblicz_silnie(n)
print("Wartość", n, "! to:", silnia)
