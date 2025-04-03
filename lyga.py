import re

def odwrotność_modulo(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

# Funkcja szyfrująca szyfrem afinicznym
def szyfruj_afinicznie(tekst, A, B):
    zaszyfrowany = "".join(
        chr(((A * (ord(znak) - ord('a')) + B) % 26) + ord('a')) if znak.isalpha() else znak for znak in tekst
    )
    return zaszyfrowany

# Funkcja deszyfrująca szyfr afiniczny
def deszyfruj_afinicznie(tekst, A, B):
    A_odwrotne = odwrotność_modulo(A, 26)  # Obliczamy odwrotność modularną A względem 26
    odszyfrowany = "".join(
        chr(((A_odwrotne * ((ord(znak) - ord('a')) - B)) % 26) + ord('a')) if znak.isalpha() else znak for znak in tekst
    )
    return odszyfrowany

# Zadanie 1: Znalezienie słów zaczynających się i kończących na 'd'
def zadanie1():
    with open("tekst.txt", "r", encoding="utf-8") as plik:
        słowa = plik.read().split()
    return [słowo for słowo in słowa if len(słowo) > 1 and słowo[0] == 'd' and słowo[-1] == 'd']

# Zadanie 2: Szyfrowanie słów o długości >= 10 kluczem (5,2)
def zadanie2():
    with open("tekst.txt", "r", encoding="utf-8") as plik:
        słowa = plik.read().split()
    return [szyfruj_afinicznie(słowo, 5, 2) for słowo in słowa if len(słowo) >= 10]

# Zadanie 3: Znajdowanie klucza szyfrującego i deszyfrującego
def zadanie3():
    with open("probka.txt", "r", encoding="utf-8") as plik:
        próbki = [wiersz.split() for wiersz in plik.readlines()]
    
    klucze = []
    for jawny, zaszyfrowany in próbki:
        for A in range(1, 26, 2):  # Przeszukujemy tylko liczby względnie pierwsze z 26
            if odwrotność_modulo(A, 26) is None:
                continue
            for B in range(26):
                if szyfruj_afinicznie(jawny, A, B) == zaszyfrowany:
                    A_deszyfrujące = odwrotność_modulo(A, 26)
                    B_deszyfrujące = (-B * A_deszyfrujące) % 26
                    klucze.append(((A, B), (A_deszyfrujące, B_deszyfrujące)))
                    break
    return klucze

# Zapis wyników
def zapisz_wyniki():
    wyniki1 = zadanie1()
    wyniki2 = zadanie2()
    wyniki3 = zadanie3()
    
    with open("wyniki.txt", "w", encoding="utf-8") as plik:
        plik.write("75.1\n" + " ".join(wyniki1) + "\n")
        plik.write("75.2\n" + "\n".join(wyniki2) + "\n")
        plik.write("75.3\n")
        for szyfr, deszyfr in wyniki3:
            plik.write(f"Klucz szyfrujący: {szyfr}, Klucz deszyfrujący: {deszyfr}\n")

zapisz_wyniki()
