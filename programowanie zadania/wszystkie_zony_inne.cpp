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

void odp(int k, const vector<vector<int>>& malzenstwa)
{
    for (int i = 0; i < k; ++i)
    {
        int x;
        cin >> x;
        const auto& partnerzy = malzenstwa[x];
        cout << partnerzy.size() << ": ";
        for (const auto& malzenstwo : partnerzy)
        {
            cout << malzenstwo << " ";
        }
        cout << endl;
    }
}

int main() {
    int s, m;
    cin >> s >> m;

    vector<vector<int>> malzenstwa(s + 1);

    wczytywanie(m, malzenstwa);

    int k;
    cin >> k;

    odp(k, malzenstwa);

    return 0;
}