#include <iostream>
#include <vector>

using namespace std;

void wczytywanie(int m, vector<vector<int>>& malzenstwa)
{
    for (int i = 0; i < m; ++i)
    {
        int a, b;
        cin >> a >> b;
        malzenstwa[b].push_back(a);
    }
}

void DFS(int x, const vector<vector<int>>& malzenstwa, vector<bool>& odwiedzone, vector<int>& partnerzy)
{
    odwiedzone[x] = true;
    partnerzy.push_back(x);

    for (const int& partner : malzenstwa[x])
    {
        if (!odwiedzone[partner])
        {
            DFS(partner, malzenstwa, odwiedzone, partnerzy);
        }
    }
}

void odp(int k, const vector<vector<int>>& malzenstwa)
{
    for (int i = 0; i < k; ++i)
    {
        int x;
        cin >> x;

        vector<bool> odwiedzone(malzenstwa.size(), false);
        vector<int> partnerzy;

        DFS(x, malzenstwa, odwiedzone, partnerzy);

        cout << partnerzy.size() - 1 << ": ";
        for (size_t j = 1; j < partnerzy.size(); ++j)
        {
            cout << partnerzy[j] << " ";
        }
        cout << endl;
    }
}

int main()
{
    int s, m;
    cin >> s >> m;

    vector<vector<int>> malzenstwa(s + 1);

    wczytywanie(m, malzenstwa);

    int k;
    cin >> k;

    odp(k, malzenstwa);

    return 0;
}