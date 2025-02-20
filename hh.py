def policz_cyfre_6(nazwa_pliku):
    try:
        with open(nazwa_pliku, 'r') as plik:
            liczby = [linia.strip() for linia in plik if linia.strip()]

        if not liczby:
            return 0, 0

        liczba_szostek_10 = sum(str(liczba).count('6') for liczba in liczby)
        liczba_szostek_8 = sum(oct(int(float(liczba))).count('6') for liczba in liczby if float(liczba).is_integer())

        return liczba_szostek_10, liczba_szostek_8

    except Exception as e:
        print(f"Błąd: {e}")
        return 0, 0

plik_nazwa = "dane.txt"
liczba_szostek_10, liczba_szostek_8 = policz_cyfre_6(plik_nazwa)

print(f"Liczba wystąpień cyfry 6 w systemie dziesiętnym: {liczba_szostek_10}")
print(f"Liczba wystąpień cyfry 6 w systemie ósemkowym: {liczba_szostek_8}")