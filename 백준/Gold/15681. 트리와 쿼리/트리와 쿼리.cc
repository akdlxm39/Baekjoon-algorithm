#include <iostream>
#include <vector>

using namespace std;

int n, r, q;
vector<int> adj_list[100'001];
int childCnt[100'001];

int makeTree(int cur, int par)
{
    int ret = 1;
    for (int nxt : adj_list[cur])
        if (nxt != par)
            ret += makeTree(nxt, cur);
    return childCnt[cur] = ret;
}

void solve()
{
    cin >> n >> r >> q;
    int u, v;
    for (int i = 0; i < n - 1; ++i)
    {
        cin >> u >> v;
        adj_list[u].push_back(v);
        adj_list[v].push_back(u);
    }
    makeTree(r, 0);
    for (int i = 0; i < q; ++i)
    {
        cin >> u;
        cout << childCnt[u] << '\n';
    }
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    solve();

    return 0;
}