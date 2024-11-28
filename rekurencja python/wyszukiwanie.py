lista = [1,3,7,11,13,17,23]

cel = 17

def szukaj(lista, cel, pozycja):

if lista[pozycja] == cel:

print("Znalazłem na pozycji", pozycja)

return

elif pozycja == len(lista)-1:

print("Nie znalazłam celu")

return

szukaj(lista, cel, pozycja+1)

szukaj(lista, cel, 0)

