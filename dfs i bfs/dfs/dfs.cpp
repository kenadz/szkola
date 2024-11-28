#include <iostream>
#include <vector>
using namespace std;

vector<vector<int>> graf(9);
vector<bool> odwiedzone(9, false);

void DFS(int v)
{
    char litera = v + 'A';
    cout << "Odwiedzam wierzchołek: " << char(v + 'A') << endl;
    odwiedzone[v] = true;
    
    for (int i = 0; i < graf[v].size(); i++)
    {
        int sasiad = graf[v][i];
        if (!odwiedzone[sasiad])
        {
            DFS(sasiad);
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

    DFS(0); // Startujemy od wierzchołka A

    return 0;
}
