// https://www.acmicpc.net/problem/11437 LCA
#include<bits/stdc++.h>
using namespace std;

const int MAX = 50001;

int n, m, parent[MAX], depth[MAX];
vector<int> adj[MAX];

void make_tree() {
    fill(parent, parent + MAX, -1);
    fill(depth, depth + MAX, -1);
    queue<int> q;
    q.push(1);
    parent[1] = 0;
    depth[1] = 1;
    while (!q.empty()) {
        int cur = q.front();
        q.pop();
        for (int &nxt: adj[cur]) {
            if (parent[nxt] == -1) {
                parent[nxt] = cur;
                depth[nxt] = depth[cur] + 1;
                q.push(nxt);
            }
        }
    }
}

int get_lca(int x, int y) {
    if (depth[x] > depth[y]) swap(x, y);
    if (x == 1) return 1;
    while (depth[x] != depth[y])
        y = parent[y];
    if (x == y) return x;
    while (parent[x] != parent[y]) {
        x = parent[x];
        y = parent[y];
    }
    return parent[x];
}

void solve() {
    cin >> n;
    for (int i = 1, u, v; i < n; ++i) {
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }
    make_tree();

    cin >> m;
    for (int i = 0, x, y; i < m; ++i) {
        cin >> x >> y;
        cout << get_lca(x, y) << '\n';
    }
}


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int t = 1;
    while (t--) solve();
    return 0;
}
