// https://www.acmicpc.net/problem/1939 중량제한
#include<bits/stdc++.h>
using namespace std;

const int MAX = 10001, INF = 1000000000;

vector<tuple<int, int, int> > bridges;
int root[MAX];
int n, m;

int find(int x) { return x == root[x] ? x : root[x] = find(root[x]); }
void union_(int u, int v) { root[find(u)] = find(v); }

void solve() {
    cin >> n >> m;
    for (int i = 0, u, v, w; i < m; ++i) {
        cin >> u >> v >> w;
        bridges.emplace_back(w, u, v);
    }

    sort(bridges.rbegin(), bridges.rend());
    for (int i = 1; i <= n; ++i) root[i] = i;
    int s, t, ans = 0;
    cin >> s >> t;
    for (auto &[w, u, v]: bridges) {
        union_(u, v);
        if (find(s) == find(t)) {
            cout << w << '\n';
            break;
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
