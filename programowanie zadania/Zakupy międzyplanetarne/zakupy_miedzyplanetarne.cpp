#include <iostream>
#include <string>
#include <cctype>
#include <cmath>

using namespace std;

int konwertujNaDziesietny(const string& liczba, int podstawa_poczatek) {
    int wartosc_dziesietna = 0;
    int dlugosc = liczba.length();

    for (int i = 0; i < dlugosc; ++i) {
        char cyfra = liczba[dlugosc - 1 - i];
        int wartosc_cyfry;
        if (isdigit(cyfra)) {
            wartosc_cyfry = cyfra - '0';
        } else {
            wartosc_cyfry = toupper(cyfra) - 'A' + 10;
        }
        wartosc_dziesietna += wartosc_cyfry * pow(podstawa_poczatek, i);
    }

    return wartosc_dziesietna;
}

string KonwertujZDziesietnego(int wartosc_dziesietna, int podstawa_koniec) {
    if (wartosc_dziesietna == 0) return "0";
    
    string wynik = "";
    while (wartosc_dziesietna > 0) {
        int reszta = wartosc_dziesietna % podstawa_koniec;
        if (reszta < 10) {
            wynik += (char)(reszta + '0');
        } else {
            wynik += (char)(reszta - 10 + 'A');
        }
        wartosc_dziesietna /= podstawa_koniec;
    }

    string wynik_odwrocony = "";
    for (int i = wynik.length() - 1; i >= 0; --i) {
        wynik_odwrocony += wynik[i];
    }
    return wynik_odwrocony;
}

int main() {
    string liczba;
    int podstawa_poczatek, podstawa_koniec;

    cout << "Podaj liczbe: ";
    cin >> liczba;
    cout << "Podaj podstawe systemu zrodlowego: ";
    cin >> podstawa_poczatek;
    cout << "Podaj podstawe systemu docelowego: ";
    cin >> podstawa_koniec;

    int wartosc_dziesietna = konwertujNaDziesietny(liczba, podstawa_poczatek);
    string wynik = KonwertujZDziesietnego(wartosc_dziesietna, podstawa_koniec);

    cout << "Liczba w systemie docelowym: " << wynik << endl;

    return 0;
}
