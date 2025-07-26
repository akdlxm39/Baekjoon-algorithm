#include <bits/stdc++.h>
#include <unordered_map>
#include <unordered_set>
#define INF 1000000001
#define LLINF 9000000000000000000
#define FAST_IO ios::sync_with_stdio(false); cin.tie(0); cout.tie(0)
#define DIR const vector<pair<int, int>> dir = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}}
#define DIR8 const vector<pair<int, int>> dir = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}, {1, 1}, {1, -1}, {-1, 1}, {-1, -1}}
#define MOD 1000000007
#define LL long long
#define pii pair<int, int>
using namespace std;
const pii operator+(const pii& a, const pii& b) { return { a.first + b.first, a.second + b.second }; }
set<pii> ans;
vector<int> visited;
vector<vector<int>> graph;
int v, e, cnt = 0;
pii makepair(int a, int b) {
    if (a > b)swap(a, b);
    return { a,b };
}
int dfs(int prev, int cur) {
    visited[cur] = ++cnt;
    int ret = visited[cur];
    for (int next : graph[cur]) {
        if (prev == next) continue;
        if (visited[next] == 0) {
            int subtree = dfs(cur, next);
            if (subtree > visited[cur]) ans.insert(makepair(cur, next));
            ret = min(ret, subtree);
        }
        else ret = min(ret, visited[next]);
    }
    return ret;
}
int main() {
    FAST_IO;
    cin >> v >> e;
    graph.resize(v + 1);
    visited.resize(v + 1);
    while (e--) {
        int a, b;
        cin >> a >> b;
        graph[a].push_back(b);
        graph[b].push_back(a);
    }
    dfs(0, 1);
    cout << ans.size() << '\n';
    for (const pii& p : ans) cout << p.first << ' ' << p.second << '\n';
}