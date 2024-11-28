a = int(input("Podaj liczbę a: "))
suma_kwadratow = sum([i**2 for i in range(1, a+1)])
print("Suma kwadratów liczb od 1 do a: ", suma_kwadratow)
