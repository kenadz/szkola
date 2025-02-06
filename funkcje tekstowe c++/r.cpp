#include <iostream>
#include <vector>
#include <queue>
#include <fstream>
#include <limits>

using namespace std;

const int INF = numeric_limits<int>::max();
using PII = pair<int, int>;

struct Edge {
    int to, distance, time;
};

using Graph = vector<vector<Edge>>;

// Algorytm Dijkstry dla dowolnej wagi (dystans/czas)
vector<int> dijkstra(const Graph& graph, int start, bool byDistance) {
    int n = graph.size();
    vector<int> dist(n, INF);
    priority_queue<PII, vector<PII>, greater<>> pq;

    dist[start] = 0;
    pq.emplace(0, start);

    while (!pq.empty()) {
        auto [d, u] = pq.top(); pq.pop();
        if (d > dist[u]) continue;

        for (const auto& edge : graph[u]) {
            int weight = byDistance ? edge.distance : edge.time;
            if (dist[u] + weight < dist[edge.to]) {
                dist[edge.to] = dist[u] + weight;
                pq.emplace(dist[edge.to], edge.to);
            }
        }
    }
    return dist;
}

int main() {
    string filename;
    cout << "Podaj nazwę pliku: ";
    cin >> filename;

    ifstream file(filename);
    if (!file) {
        cerr << "Nie można otworzyć pliku!\n";
        return 1;
    }

    int n, m;
    file >> n >> m;
    Graph graph(n);

    for (int i = 0; i < m; i++) {
        int u, v, d, t;
        file >> u >> v >> d >> t;
        graph[u].push_back({v, d, t});
    }

    file.close();

    int start, end;
    cout << "Podaj wierzchołek początkowy i końcowy: ";
    cin >> start >> end;

    vector<int> dist = dijkstra(graph, start, true);
    vector<int> time = dijkstra(graph, start, false);

    cout << "Najkrótsza droga do " << end << ": " << (dist[end] == INF ? -1 : dist[end]) << " jednostek odległości\n";
    cout << "Najszybsza droga do " << end << ": " << (time[end] == INF ? -1 : time[end]) << " jednostek czasu\n";

    return 0;
}