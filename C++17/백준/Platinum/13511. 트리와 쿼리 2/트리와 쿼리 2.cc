// https://www.acmicpc.net/problem/13511 트리와 쿼리 2
#include<bits/stdc++.h>
using namespace std;

typedef long long ll;

const ll MAX = 100'001LL;

ll n, m, depth;
vector<array<ll, 2> > adj[MAX];
vector<array<ll, 2> > parent[20];
vector<ll> level;

void make_tree(ll root = 1) {
    parent[0].resize(n + 1, {-1, 0});
    level.resize(n + 1, -1);
    queue<ll> q;
    q.push(root);
    parent[0][root] = {root, 0};
    level[root] = 1;
    ll cur = 1;
    while (!q.empty()) {
        cur = q.front();
        q.pop();
        for (auto &[nxt, cost]: adj[cur]) {
            if (parent[0][nxt][0] == -1) {
                parent[0][nxt] = {ll(cur), ll(cost)};
                level[nxt] = level[cur] + 1;
                q.push(nxt);
            }
        }
    }

    depth = ll(log2(level[cur] - 1)) + 1;
    for (ll k = 1; k <= depth; ++k) {
        parent[k].resize(n + 1, {-1, 0});
        for (ll i = 1; i <= n; ++i) {
            ll j = parent[k - 1][i][0];
            parent[k][i][0] = parent[k - 1][j][0];
            parent[k][i][1] = parent[k - 1][i][1] + parent[k - 1][j][1];
        }
    }
}


ll query1(ll u, ll v) {
    ll ret = 0LL;
    if (level[u] < level[v]) swap(u, v);
    while (int level_gap = level[u] - level[v]) {
        ll move = ll(log2(level_gap));
        ret += parent[move][u][1];
        u = parent[move][u][0];
    }
    while (u != v) {
        ll k = depth;
        while (parent[k][u][0] == parent[k][v][0] && --k);
        ret += parent[k][u][1] + parent[k][v][1];
        u = parent[k][u][0], v = parent[k][v][0];
    }
    return ret;
}

ll query2(ll uu, ll vv, ll x) {
    ll u = uu, v = vv;
    if (level[u] < level[v])
        swap(u, v);
    while (ll level_gap = level[u] - level[v])
        u = parent[ll(log2(level_gap))][u][0];
    while (u != v) {
        ll k = depth;
        while (parent[k][u][0] == parent[k][v][0] && --k);
        u = parent[k][u][0], v = parent[k][v][0];
    }
    if (x <= level[uu] - level[u]) {
        ll u_ = uu;
        ll gap = 0;
        while (x) {
            if (x & 1)
                u_ = parent[gap][u_][0];
            x >>= 1;
            gap++;
        }
        return u_;
    }
    x = level[uu] - level[u] + level[vv] - level[v] - x;
    ll v_ = vv;
    ll gap = 0;
    while (x) {
        if (x & 1)
            v_ = parent[gap][v_][0];
        x >>= 1;
        gap++;
    }
    return v_;
}

void solve() {
    cin >> n;
    for (int i = 1; i < n; ++i) {
        ll u, v, w;
        cin >> u >> v >> w;
        adj[u].push_back({v, w});
        adj[v].push_back({u, w});
    }
    make_tree();
    cin >> m;
    for (int i = 0, x; i < m; ++i) {
        ll u, v, k;
        cin >> x >> u >> v;
        if (x == 1) {
            cout << query1(u, v) << '\n';
        } else {
            cin >> k;
            cout << query2(u, v, k - 1) << '\n';
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int t = 1;
    while (t--) solve();
    return 0;
}
