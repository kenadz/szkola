def najlepsza_suma(lista):
    sumaTeraz = 0
    sumaMax = 0
    start = koniec = s = 0

    for i in range(len(lista)):
        if sumaTeraz < 0:
            sumaTeraz = lista[i]
            s = i
        else:
            sumaTeraz += lista[i]

        if sumaMax < sumaTeraz:
            sumaMax = sumaTeraz
            start = s
            koniec = i

    max_podciag = lista[start:koniec + 1]
    print(sumaMax, max_podciag)


lista = [-10, 5, 1, 6, -9, 2, -7, 3, -5]
najlepsza_suma(lista)
