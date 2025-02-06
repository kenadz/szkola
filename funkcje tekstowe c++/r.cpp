#include <iostream>
#include <vector>
#include <limits>

using namespace std;

const int INF = numeric_limits<int>::max();

struct Krawedz {
    int do_, waga;
};

using Graf = vector<vector<Krawedz>>;

vector<int> dijkstra(const Graf& graf, int pocz) {
    int n = graf.size();
    vector<int> koszt(n, INF);
    vector<bool> odwiedzone(n, false);

    koszt[pocz] = 0;

    for (int i = 0; i < n - 1; i++) {
        int w1 = -1;
        for (int j = 0; j < n; j++) {
            if (!odwiedzone[j] && (w1 == -1 || koszt[j] < koszt[w1])) {
                w1 = j;
            }
        }

        if (koszt[w1] == INF) break;

        odwiedzone[w1] = true;

        for (const auto& krawedz : graf[w1]) {
            int w2 = krawedz.do_;
            int waga = krawedz.waga;

            if (!odwiedzone[w2] && koszt[w1] + waga < koszt[w2]) {
                koszt[w2] = koszt[w1] + waga;
            }
        }
    }

    return koszt;
}

int main() {
    int n, m, pocz;
    cin >> n >> m;

    Graf graf(n);

    for (int i = 0; i < m; i++) {
        int u, v, w;
        cin >> u >> v >> w;
        graf[u].push_back({v, w});
    }

    cin >> pocz;

    vector<int> koszt = dijkstra(graf, pocz);

    for (int i = 0; i < n; i++) {
        cout << (koszt[i] == INF ? -1 : koszt[i]) << "\n";
    }

    return 0;
}