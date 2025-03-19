def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_semiprime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            j = n // i
            return is_prime(i) and is_prime(j)
    return False

def binary_to_decimal(binary_str):
    return int(binary_str, 2)

def zadanie_63_1(ciagi):
    dwucykliczne = []
    for ciag in ciagi:
        dlugosc = len(ciag)
        if dlugosc % 2 == 0:
            polowa = dlugosc // 2
            if ciag[:polowa] == ciag[polowa:]:
                dwucykliczne.append(ciag)
    return dwucykliczne

def zadanie_63_2(ciagi):
    liczba_ciagow = 0
    for ciag in ciagi:
        if "11" not in ciag:
            liczba_ciagow += 1
    return liczba_ciagow

def zadanie_63_3(ciagi):
    liczby_polpierwsze = []
    for ciag in ciagi:
        liczba = binary_to_decimal(ciag)
        if is_semiprime(liczba):
            liczby_polpierwsze.append(liczba)
    return liczby_polpierwsze

with open("ciagi.txt", "r") as file:
    ciagi = [line.strip() for line in file]

wynik_63_1 = zadanie_63_1(ciagi)
wynik_63_2 = zadanie_63_2(ciagi)
wynik_63_3 = zadanie_63_3(ciagi)

min_polpierwsza = min(wynik_63_3) if wynik_63_3 else 0
max_polpierwsza = max(wynik_63_3) if wynik_63_3 else 0

with open("wyniki_ciagi.txt", "w") as file:
    file.write("63.1\n")
    for ciag in wynik_63_1:
        file.write(ciag + "\n")
    
    file.write("\n63.2\n")
    file.write(str(wynik_63_2) + "\n")
    
    file.write("\n63.3\n")
    file.write(f"Liczba ciągów reprezentujących liczby półpierwsze: {len(wynik_63_3)}\n")
    file.write(f"Najmniejsza liczba półpierwsza: {min_polpierwsza}\n")
    file.write(f"Największa liczba półpierwsza: {max_polpierwsza}\n")
