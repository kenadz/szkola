#include <iostream>
#include <fstream>
#include <vector>
#include <stack>
using namespace std;

void dfs_iteracyjny(vector<vector<int>> &graf, int start) {
    vector<bool> odwiedzone(graf.size(), false);
    stack<int> stos;
    stos.push(start);

    cout << "Odwiedzone wierzchołki: ";
    while (!stos.empty()) {
        int wierzcholek = stos.top();
        stos.pop();

        if (!odwiedzone[wierzcholek]) {
            odwiedzone[wierzcholek] = true;
            cout << wierzcholek << " ";

            for (auto it = graf[wierzcholek].rbegin(); it != graf[wierzcholek].rend(); ++it) {
                if (!odwiedzone[*it]) {
                    stos.push(*it);
                }
            }
        }
    }
    cout << endl;
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

    int start;
    cout << "Podaj wierzcholek startowy: ";
    cin >> start;

    dfs_iteracyjny(graf, start);

    return 0;
}