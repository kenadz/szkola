#include <iostream>
#include <fstream>
#include <vector>
#include <queue>
using namespace std;

void bfs(vector<vector<int>> &graf, vector<bool> &odwiedzone, int start) {
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
        graf[v].push_back(u);
    }

    vector<bool> odwiedzone(liczba_wierzcholkow, false);
    bfs(graf, odwiedzone, 0);

    for (bool odwiedzony : odwiedzone) {
        if (!odwiedzony) {
            cout << "Graf nie jest spojny" << endl;
            return 0;
        }
    }
    cout << "Graf jest spojny" << endl;

    return 0;
}