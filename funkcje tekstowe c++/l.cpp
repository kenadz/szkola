#include <iostream>
#include <vector>
#include <queue>
using namespace std;

bool czyIstniejeCyklZawierajacyWierzcholek(vector<vector<int>>& graf, int start) {
    int liczbaWierzcholkow = graf.size();
    vector<bool> odwiedzone(liczbaWierzcholkow, false);
    vector<bool> wStosie(liczbaWierzcholkow, false);
    queue<int> kolejka;
    kolejka.push(start);

    while (!kolejka.empty()) {
        int wierzcholek = kolejka.front();
        kolejka.pop();

        if (!odwiedzone[wierzcholek]) {
            odwiedzone[wierzcholek] = true;
            wStosie[wierzcholek] = true;
        }

        for (int sasiad : graf[wierzcholek]) {
            if (!odwiedzone[sasiad]) {
                kolejka.push(sasiad);
            } else if (wStosie[sasiad]) {
                return true;
            }
        }
        wStosie[wierzcholek] = false;
    }
    return false;
}

int main() {
    int liczbaWierzcholkow, liczbaKrawedzi, start;
    cin >> liczbaWierzcholkow >> liczbaKrawedzi;

    vector<vector<int>> graf(liczbaWierzcholkow);
    for (int i = 0; i < liczbaKrawedzi; ++i) {
        int poczatek, koniec;
        cin >> poczatek >> koniec;
        graf[poczatek].push_back(koniec);
    }

    cin >> start;
    if (czyIstniejeCyklZawierajacyWierzcholek(graf, start)) {
        cout << "Cykl istnieje" << endl;
    } else {
        cout << "Brak cyklu" << endl;
    }

    return 0;
}