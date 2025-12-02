// https://www.acmicpc.net/problem/1043 거짓말
#include<bits/stdc++.h>
using namespace std;

int n, m, l, x, ans;
vector<vector<int> > adj;
vector<bool> visited;
queue<int> q;

void solve() {
    cin >> n >> m >> l;
    ans = m;
    adj.resize(n + m + 1);
    visited.resize(n + m + 1);
    while (l--) {
        cin >> x;
        visited[x] = true;
        q.push(x);
    }
    for (int i = n + 1; i <= n + m; ++i) {
        cin >> l;
        while (l--) {
            cin >> x;
            adj[i].push_back(x);
            adj[x].push_back(i);
        }
    }
    while (!q.empty()) {
        int cur = q.front();
        q.pop();
        for (auto &nxt: adj[cur]) {
            if (visited[nxt]) continue;
            if (nxt > n) --ans;
            visited[nxt] = true;
            q.push(nxt);
        }
    }
    cout << ans << '\n';
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int t = 1;
    while (t--) solve();
    return 0;
}
