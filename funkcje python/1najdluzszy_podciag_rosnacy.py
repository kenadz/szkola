def najdluzszy_ciag_rosnacy(lista):
    max_dl = 1
    poczatek = p = 0
    dl = 1

    for i in range(1, len(lista)):
        if lista[i] > lista[i - 1]:
            dl += 1
            if dl > max_dl:
                max_dl = dl
                poczatek = p
        else:
            p = i
            dl = 1

    wynik = lista[poczatek:poczatek + max_dl]
    print(wynik)


lista = [1, 2, 3, 3, 2, 4, 5, 7, 0, 9]
najdluzszy_ciag_rosnacy(lista)
