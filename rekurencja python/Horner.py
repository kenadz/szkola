def horner(lista_wspolczynnikow, nr, x): # współczynniki, nr współczynnika, wartość
    if nr == 0:
        return lista_wspolczynnikow[0]
    return x*horner(lista_wspolczynnikow, nr - 1, x) + lista_wspolczynnikow[nr]

# główna część programu

wsp = input("Podaj współczynniki wielomianu: ").split()

# rzutujemy listę napisów na listę liczb całkowitych
for i in range(len(wsp)):
    wsp[i] = int(wsp[i])

x = int(input("Podaj wartość wielomianu: "))

print(f"Wartość wielomianu o współczynnikach {wsp} w punkcie {x} wynosi", horner(wsp, len(wsp) - 1, x))
