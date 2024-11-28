#include <iostream>
#include <vector>
#include <queue>
using namespace std;

vector<vector<int>> graf(9);
vector<bool> odwiedzone(9, false);

void BFS(int v) {
    queue<int> kolejka;
    kolejka.push(v);
    odwiedzone[v] = true;

    while (!kolejka.empty()) {
        int aktualny = kolejka.front();
        kolejka.pop();
        char litera = aktualny + 'A';
        cout << "Odwiedzam wierzchołek: " << litera << endl;

        for (int sasiad : graf[aktualny]) {
            if (!odwiedzone[sasiad]) {
                kolejka.push(sasiad);
                odwiedzone[sasiad] = true;
            }
        }
    }
}

int main() {
    // lista sąsiedztwa
    graf[0] = {1, 4}; // A -> B, E
    graf[1] = {2, 3}; // B -> C, D
    graf[4] = {5};    // E -> F
    graf[5] = {6, 7}; // F -> G, H
    graf[7] = {8};    // H -> I

    BFS(0); // Startujemy od wierzchołka A

    return 0;
}
