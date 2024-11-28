a = int(input("Podaj liczbę naturalną a: "))
i = 1
while i * i <= a:
    i += 1
czesc_calkowita_pierwiastka = i - 1
print("Część całkowita pierwiastka kwadratowego z", a, "to:", czesc_calkowita_pierwiastka)
