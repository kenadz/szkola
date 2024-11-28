#include <iostream>
#include <vector>
#include <string>

using namespace std;

string dziesietnyNaPiatkowy(int n) {
    if (n == 0) {
        return "0";
    }

    vector<int> cyfry;
    while (n > 0) {
        int reszta = n % 5;
        cyfry.push_back(reszta);
        n /= 5;
    }

    string wynik = "";
    for (int i = cyfry.size() - 1; i >= 0; --i) {
        wynik += to_string(cyfry[i]);
    }

    return wynik;
}

int main() {
    cout << dziesietnyNaPiatkowy(42) << endl;
    cout << dziesietnyNaPiatkowy(517) << endl;

    return 0;
}