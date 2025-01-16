#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

bool dfs(vector<vector<int>> &graf, vector<bool> &odwiedzone, vector<bool> &stos, int wierzcholek) {
    odwiedzone[wierzcholek] = true;
    stos[wierzcholek] = true;

    for (int sasiad : graf[wierzcholek]) {
        if (!odwiedzone[sasiad]) {
            if (dfs(graf, odwiedzone, stos, sasiad)) return true;
        } else if (stos[sasiad]) {
            return true;
        }
    }
    stos[wierzcholek] = false;
    return false;
}

int main() {
    ifstream plik("graf_2.txt");
    int liczba_wierzcholkow, liczba_krawedzi;
    plik >> liczba_wierzcholkow >> liczba_krawedzi;

    vector<vector<int>> graf(liczba_wierzcholkow);
    for (int i = 0; i < liczba_krawedzi; i++) {
        int u, v;
        plik >> u >> v;
        graf[u].push_back(v);
    }

    vector<bool> odwiedzone(liczba_wierzcholkow, false);
    vector<bool> stos(liczba_wierzcholkow, false);

    for (int i = 0; i < liczba_wierzcholkow; i++) {
        if (!odwiedzone[i] && dfs(graf, odwiedzone, stos, i)) {
            cout << "Cykl istnieje" << endl;
            return 0;
        }
    }
    cout << "Cykl nie istnieje" << endl;

    return 0;
}