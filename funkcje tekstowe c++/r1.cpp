#include <iostream>
#include <fstream>
#include <vector>
#include <queue>
#include <limits>

using namespace std;

const int INF = numeric_limits<int>::max();

struct Krawedz {
    int do_, odleglosc, czas;
};

using Graf = vector<vector<Krawedz>>;

vector<int> dijkstra(const Graf& graf, int pocz, bool czas) {
    int n = graf.size();
    vector<int> koszt(n, INF);
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<>> pq;

    koszt[pocz] = 0;
    pq.push({0, pocz});

    while (!pq.empty()) {
        int akt_koszt = pq.top().first;
        int wierz = pq.top().second;
        pq.pop();

        if (akt_koszt > koszt[wierz]) continue;

        for (const auto& krawedz : graf[wierz]) {
            int nowy_koszt = akt_koszt + (czas ? krawedz.czas : krawedz.odleglosc);

            if (nowy_koszt < koszt[krawedz.do_]) {
                koszt[krawedz.do_] = nowy_koszt;
                pq.push({nowy_koszt, krawedz.do_});
            }
        }
    }

    return koszt;
}

int main() {
    string nazwa_pliku;
    cout << "Podaj nazwę pliku: ";
    cin >> nazwa_pliku;

    ifstream plik(nazwa_pliku);
    if (!plik) {
        cerr << "Nie można otworzyć pliku!\n";
        return 1;
    }

    int n, m;
    plik >> n >> m;

    Graf graf(n);

    for (int i = 0; i < m; i++) {
        int u, v, odleglosc, czas;
        plik >> u >> v >> odleglosc >> czas;
        graf[u].push_back({v, odleglosc, czas});
    }

    plik.close();

    int pocz, koniec;
    cout << "Podaj wierzchołek początkowy i końcowy: ";
    cin >> pocz >> koniec;

    vector<int> najkrotsza = dijkstra(graf, pocz, false);
    vector<int> najszybsza = dijkstra(graf, pocz, true);

    cout << "Najkrótsza droga: " << (najkrotsza[koniec] == INF ? -1 : najkrotsza[koniec]) << "\n";
    cout << "Najkrótszy czas: " << (najszysza[koniec] == INF ? -1 : najszybsza[koniec]) << "\n";

    return 0;
}