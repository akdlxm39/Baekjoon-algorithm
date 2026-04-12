#include <iostream>
#include <queue>
#include <unordered_set>

using namespace std;

constexpr int INF = int(1e9);

unordered_set<int> adj_list[101];
int dist[101];
int start, ans;

int bfs()
{
    queue<int> q;
    q.push(start);
    dist[start] = 0;
    int max_dist = -1, ret;
    while (!q.empty())
    {
        int cur = q.front();
        q.pop();
        if (max_dist < dist[cur])
        {
            max_dist = dist[cur];
            ret = cur;
        }
        else if (max_dist == dist[cur] && ret < cur)
        {
            ret = cur;
        }
        for (int nxt : adj_list[cur])
        {
            if (dist[nxt] == INF)
            {
                q.push(nxt);
                dist[nxt] = dist[cur] + 1;
            }
        }
    }
    return ret;
}

void init()
{
    for (int i = 1; i <= 100; ++i)
    {
        dist[i] = INF;
        adj_list[i].clear();
    }
}

void input()
{
    int n;
    cin >> n >> start;
    n >>= 1;
    for (int i = 0; i < n; ++i)
    {
        int from, to;
        cin >> from >> to;
        adj_list[from].insert(to);
    }
}

void solve()
{
    ans = bfs();
}

void output(int testCase)
{
    cout << '#' << testCase << ' ' << ans << '\n';
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int T = 10;
    for (int testCase = 1; testCase <= T; ++testCase)
    {
        init();
        input();
        solve();
        output(testCase);
    }

    return 0;
}