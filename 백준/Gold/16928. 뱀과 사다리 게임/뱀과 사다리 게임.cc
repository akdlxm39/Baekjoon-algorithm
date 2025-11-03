//
#include<bits/stdc++.h>
using namespace std;

const int MAX = 101;

int n, m, adj[MAX], counts[MAX];

int bfs() {
    fill(counts, counts + MAX, -1);
    queue<int> q;
    q.push(1);
    counts[1] = 0;
    while (!q.empty()) {
        int cur = q.front();
        q.pop();
        for (int d = 1; d <= 6; ++d) {
            int nxt = adj[cur + d] ? adj[cur + d] : cur + d;
            if (counts[nxt] == -1) {
                counts[nxt] = counts[cur] + 1;
                if (nxt == 100) return counts[nxt];
                q.push(nxt);
            }
        }
    }
}


void solve() {
    cin >> n >> m;
    fill(adj, adj + MAX, 0);
    for (int i = 0, u, v; i < n + m; ++i) {
        cin >> u >> v;
        adj[u] = v;
    }
    cout << bfs() << '\n';
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int t = 1;
    while (t--) solve();
    return 0;
}
