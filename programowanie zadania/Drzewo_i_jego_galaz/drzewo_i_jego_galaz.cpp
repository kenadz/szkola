#include <iostream>
#include <vector>

using namespace std;

vector<vector<int>> t;

bool odw[32]; // odwiedzone wierzchołki

int DFS(int v)
{
    odw[v] = true;
    int max_odleglosc = 0;

    for (int i = 0; i < t[v].size(); i++)
    {
        if (!odw[t[v][i]])
        {
            max_odleglosc = max(max_odleglosc, DFS(t[v][i]));
        }
    }
    
    return max_odleglosc + 1;
}

int main()
{
    int w, k;
    cin >> w >> k;
    
    t.resize(w + 1);

    // for (int i = 1; i <= w; i++)
    // {
    //     cout << "t[" << i << "] = ";
    //     for (int j = 0; j < t[i].size(); j++)
    //     {
    //         cout << t[i][j] << " ";
    //     }
    //     cout << endl;
    // }

    for (int i = 0; i < k; i++)
    {
        int a, b;
        cin >> a >> b;
        t[a].push_back(b);
        t[b].push_back(a);
    }

    int najwieksza_odleglosc = DFS(1) - 1;
    cout << najwieksza_odleglosc << endl;

    return 0;
}
