#include <iostream>
#include <vector>
#include <queue>
using namespace std;

void bfs(const vector<vector<int>>& graf, int start, int n, vector<int>& odleglosci)
{
    odleglosci.assign(n + 1, -1);
    queue<int> q;
   
    q.push(start);
    odleglosci[start] = 0;
   
    while (!q.empty())
    {
        int biezacy = q.front();
        q.pop();
       
        for (int sasiad : graf[biezacy])
        {
            if (odleglosci[sasiad] == -1)
            {
                odleglosci[sasiad] = odleglosci[biezacy] + 1;
                q.push(sasiad);
            }
        }
    }
}

int main()
{
    ios::sync_with_stdio(false); // inaczej, Przekroczenie limitu czasu na szkopule
    cin.tie(nullptr);

    int n, start;
    cin >> n >> start;
    vector<vector<int>> graf(n + 1);
   
    for (int i = 0; i < n - 1; i++)
    {
        int a, b;
        cin >> a >> b;
        graf[a].push_back(b);
        graf[b].push_back(a);
    }
   
    vector<int> odleglosci;
    bfs(graf, start, n, odleglosci);
   
    for (int i = 1; i <= n; i++)
    {
        cout << odleglosci[i] << endl;
    }
   
    return 0;
}
