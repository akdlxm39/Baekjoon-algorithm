// https://www.acmicpc.net/problem/2098 외판원 순회
#include<bits/stdc++.h>
using namespace std;

const int INF = 16'000'007;

int n, weights[16][16], dp[16][65536], path[16][65536];

void minimum(int mask, int i) {
    int min_value = INF, min_j = 0;
    for (int j = 1; j < n; ++j) {
        if (mask & (1 << j)) {
            int m = weights[i][j] + dp[j][mask ^ (1 << j)];
            if (min_value > m) {
                min_value = m;
                min_j = j;
            }
        }
    }
    dp[i][mask] = min_value;
    path[i][mask] = min_j;
}

void travel() {
    int bit_size = (int) pow(2, n);
    for (int i = 1; i < n; ++i)
        dp[i][0] = weights[i][0];
    for (int k = 1; k < n; ++k) {
        for (int mask = 1; mask < bit_size; ++mask) {
            if (__builtin_popcount(mask) != k) continue;
            for (int i = 1; i < n; ++i) {
                if (!(mask & (1 << i)))
                    minimum(mask, i);
            }
        }
    }
    minimum(bit_size - 2, 0);
}

void solve() {
    cin >> n;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            cin >> weights[i][j];
            if (weights[i][j] == 0 && i != j)
                weights[i][j] = INF;
        }
    }
    travel();
    cout << dp[0][(int) pow(2, n) - 2] << '\n';
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int t = 1;
    while (t--) solve();
    return 0;
}
