// https://www.acmicpc.net/problem/2098 외판원 순회
#include<bits/stdc++.h>
using namespace std;

const int INF = 100'000'007, MAX_V = 16, MAX_B = 65536;

int n, weights[MAX_V][MAX_V], dp[MAX_V][MAX_B], path[MAX_V][MAX_B];

int travel(int cur, int mask) {
    if (dp[cur][mask] != -1)
        return dp[cur][mask];
    dp[cur][mask] = INF;
    for (int nxt = 1; nxt < n; ++nxt) {
        if (mask & (1 << nxt)) continue;
        int cost = travel(nxt, mask | (1 << nxt)) + weights[cur][nxt];
        if (dp[cur][mask] > cost) {
            dp[cur][mask] = cost;
            path[cur][mask] = nxt;
        }
    }
    return dp[cur][mask];
}

void solve() {
    cin >> n;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            cin >> weights[i][j];
            if (weights[i][j] == 0)
                weights[i][j] = INF;
        }
    }
    fill_n(dp[0], MAX_B * MAX_V, -1);
    for (int i = 1; i < n; ++i) {
        dp[i][(1 << n) - 1] = weights[i][0];
    }
    cout << travel(0, 1) << '\n';
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int t = 1;
    while (t--) solve();
    return 0;
}
