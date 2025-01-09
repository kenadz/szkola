#include <iostream>
#include <vector>
#include <queue>
#include <fstream>

using namespace std;

bool czyIstniejeDroga(int start, int koniec, int n, const vector<vector<int>>& graf) {
    vector<bool> odwiedzone(n, false);
    queue<int> kolejka;

    kolejka.push(start);
    odwiedzone[start] = true;

    cout << "Rozpoczynam przeszukiwanie od wierzcholka " << start << "." << endl;

    while (!kolejka.empty()) {
        int wierzcholek = kolejka.front();
        kolejka.pop();

        cout << "Odwiedzam wierzcholek " << wierzcholek << "." << endl;

        if (wierzcholek == koniec) {
            cout << "Znaleziono wierzcholek " << koniec << "." << endl;
            return true;
        }

        for (int sasiad : graf[wierzcholek]) {
            if (!odwiedzone[sasiad]) {
                odwiedzone[sasiad] = true;
                kolejka.push(sasiad);
                cout << "Dodaje do kolejki wierzcholek " << sasiad << "." << endl;
            }
        }
    }

    cout << "Nie znaleziono drogi do wierzcholka " << koniec << "." << endl;
    return false;
}

int main() {
    ifstream plik("graf_2.txt");
    if (!plik) {
        cerr << "Blad otwarcia pliku!" << endl;
        return 1;
    }

    int n, m;
    plik >> n >> m;

    vector<vector<int>> graf(n);
    for (int i = 0; i < m; ++i) {
        int u, v;
        plik >> u >> v;
        graf[u].push_back(v);
    }

    int start, koniec;
    cout << "Podaj numer wierzcholka poczatkowego: ";
    cin >> start;
    cout << "Podaj numer wierzcholka koncowego: ";
    cin >> koniec;

    if (czyIstniejeDroga(start, koniec, n, graf)) {
        cout << "Istnieje droga z wierzcholka " << start << " do wierzcholka " << koniec << "." << endl;
    } else {
        cout << "Nie istnieje droga z wierzcholka " << start << " do wierzcholka " << koniec << "." << endl;
    }

    return 0;
}