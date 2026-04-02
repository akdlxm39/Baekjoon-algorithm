#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

const int INF = 21e8;

struct Edge
{
    int to, dist;
};
struct Node
{
    int id, dist;
    inline bool operator<(const Node &other) const
    {
        return dist > other.dist;
    }
};

int n, m, t, s, g, h;
vector<Edge> adj_list[2001];
priority_queue<Node> pq;
int dist[2001];
vector<int> ans;

void solve()
{
    for (int i = 1; i <= n; ++i)
    {
        adj_list[i].clear();
        dist[i] = INF;
    }
    pq = priority_queue<Node>();
    ans.clear();

    cin >> n >> m >> t >> s >> g >> h;
    for (int i = 0, a, b, d; i < m; ++i)
    {
        cin >> a >> b >> d;
        d = d * 2 - ((a == g && b == h) || (a == h && b == g));
        adj_list[a].push_back({b, d});
        adj_list[b].push_back({a, d});
    }
    dist[s] = 0;
    pq.push({s, 0});
    while (!pq.empty())
    {
        Node cur = pq.top();
        pq.pop();
        if (dist[cur.id] < cur.dist)
            continue;
        for (const Edge &e : adj_list[cur.id])
        {
            Node nxt = {e.to, cur.dist + e.dist};
            if (dist[nxt.id] <= nxt.dist)
                continue;
            dist[nxt.id] = nxt.dist;
            pq.push(nxt);
        }
    }
    for (int i = 0, x; i < t; ++i)
    {
        cin >> x;
        if (dist[x] & 1)
            ans.push_back(x);
    }
    sort(ans.begin(), ans.end());
    for (int x : ans)
        cout << x << ' ';
    cout << '\n';
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    for (int i = 1; i <= 2000; ++i)
        dist[i] = INF;

    int TC;
    cin >> TC;
    while (TC--)
        solve();

    return 0;
}