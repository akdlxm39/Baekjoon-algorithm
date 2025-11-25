// https://www.acmicpc.net/problem/11780 플로이드 2
#include<bits/stdc++.h>
using namespace std;

const int INF = 100'000'001;

int n, m;
vector<vector<int> > cost, pre;

void floyd_warshall() {
    for (int k = 1; k <= n; ++k) {
        for (int i = 1; i <= n; ++i) {
            if (k == i) continue;
            for (int j = 1; j <= n; ++j) {
                if (k == j) continue;
                if (cost[i][j] > cost[i][k] + cost[k][j]) {
                    cost[i][j] = cost[i][k] + cost[k][j];
                    pre[i][j] = k;
                }
            }
        }
    }
}

void traceback(int s, int e, vector<int> &tb) {
    if (pre[s][e] == s) {
        tb.push_back(s);
        return;
    }
    traceback(s, pre[s][e], tb);
    traceback(pre[s][e], e, tb);
}

void solve() {
    cin >> n >> m;
    pre.resize(n + 1);
    cost.resize(n + 1, vector(n + 1, INF));
    for (int i = 1; i <= n; ++i) {
        pre[i] = vector(n + 1, i);
        cost[i][i] = 0;
    }
    for (int i = 0, a, b, c; i < m; ++i) {
        cin >> a >> b >> c;
        if (cost[a][b] > c)
            cost[a][b] = c;
    }
    floyd_warshall();
    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= n; ++j)
            cout << (cost[i][j] != INF ? cost[i][j] : 0) << ' ';
        cout << '\n';
    }
    vector<int> v;
    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= n; ++j) {
            if (i == j || cost[i][j] == INF) {
                cout << "0\n";
                continue;
            }
            vector<int> tb;
            traceback(i, j, tb);
            tb.push_back(j);
            cout << tb.size();
            for (auto &x: tb)
                cout << ' ' << x;
            cout << '\n';
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
