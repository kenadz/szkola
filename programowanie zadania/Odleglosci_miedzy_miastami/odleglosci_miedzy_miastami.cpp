#include <iostream>
#include <vector>
using namespace std;

void bfs(const vector<vector<int>>& graf, int start, int odleglosci[], int N)
{
    bool odwiedzone[32] = {false};
    for (int i = 1; i <= N; ++i)
    {
        odleglosci[i] = -1;
    }

    odwiedzone[start] = true;
    odleglosci[start] = 0;

    vector<int> kolejka;
    kolejka.push_back(start);

    int poczatek = 0;

    while (poczatek < kolejka.size())
    {
        int biezacy = kolejka[poczatek++];
        
        for (int sasiad : graf[biezacy])
        {
            if (!odwiedzone[sasiad])
            {
                odwiedzone[sasiad] = true;
                odleglosci[sasiad] = odleglosci[biezacy] + 1;
                kolejka.push_back(sasiad);
            }
        }
    }
}

int main()
{
    int N, K;
    cin >> N >> K;

    vector<vector<int>> graf(N + 1);

    for (int i = 0; i < K; ++i)
    {
        int a, b;
        cin >> a >> b;
        graf[a].push_back(b);
        graf[b].push_back(a);
    }

    int P;
    cin >> P;
    
    vector<int> zapytania_a(P);
    vector<int> zapytania_b(P);

    for (int i = 0; i < P; ++i)
    {
        cin >> zapytania_a[i] >> zapytania_b[i];
    }

    for (int i = 0; i < P; ++i)
    {
        int a = zapytania_a[i];
        int b = zapytania_b[i];
        int odleglosci[1001];

        if (a == b)
        {
            cout << 0 << endl;
        }
        else
        {
            bfs(graf, a, odleglosci, N);
            cout << odleglosci[b] << endl;
        }
    }

    return 0;
}
