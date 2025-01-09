#include <iostream>
#include <vector>
#include <queue>
#include <fstream>

using namespace std;

void czyOsiagalne(int start, int n, const vector<vector<int>>& graf) {
    vector<bool> odwiedzone(n, false);
    queue<int> kolejka;

    kolejka.push(start);
    odwiedzone[start] = true;

    while (!kolejka.empty()) {
        int wierzcholek = kolejka.front();
        kolejka.pop();

        for (int sasiad : graf[wierzcholek]) {
            if (!odwiedzone[sasiad]) {
                odwiedzone[sasiad] = true;
                kolejka.push(sasiad);
            }
        }
    }

    // Sprawdzenie, czy wszystkie wierzchołki zostały odwiedzone
    bool wszystkieOsiagalne = true;
    for (bool odwiedzony : odwiedzone) {
        if (!odwiedzony) {
            wszystkieOsiagalne = false;
            break;
        }
    }

    if (wszystkieOsiagalne) {
        cout << "Mozna dojsc do wszystkich wierzcholkow z wierzcholka " << start << "." << endl;
    } else {
        cout << "Nie mozna dojsc do wszystkich wierzcholkow z wierzcholka " << start << "." << endl;
    }
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

    int start;
    cout << "Podaj numer wierzcholka poczatkowego: ";
    cin >> start;

    czyOsiagalne(start, n, graf);

    return 0;
}