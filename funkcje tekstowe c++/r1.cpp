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

vector<int> dijkstra(const Graf& graf, int pocz, bool tryb_czas) {
    int n = graf.size();
    vector<int> koszt(n, INF);
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;

    koszt[pocz] = 0;
    pq.push({0, pocz});

    while (!pq.empty()) {
        int akt_koszt = pq.top().first;
        int wierz = pq.top().second;
        pq.pop();

        if (akt_koszt > koszt[wierz]) {
            continue;
        }

        for (size_t i = 0; i < graf[wierz].size(); i++) {
            Krawedz krawedz = graf[wierz][i];
            int waga_krawedzi;

            if (tryb_czas) {
                waga_krawedzi = krawedz.czas;
            } else {
                waga_krawedzi = krawedz.odleglosc;
            }

            int nowy_koszt = akt_koszt + waga_krawedzi;

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

    if (najkrotsza[koniec] == INF) {
        cout << "Brak dostępnej drogi między podanymi wierzchołkami.\n";
    } else {
        cout << "Najkrótsza droga: " << najkrotsza[koniec] << "\n";
        cout << "Najkrótszy czas: " << najszybsza[koniec] << "\n";
    }

    return 0;
}