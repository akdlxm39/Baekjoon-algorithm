#include<bits/stdc++.h>
using namespace std;

typedef long long ll;

int n, a0, b0, k, total;
ll dp[501][501];

void solve() {
    cin >> n >> a0 >> b0 >> k;
    total = a0 + b0;
    for (int a = 0; a <= total; a++)
        dp[0][a] = -100000;
    dp[0][a0] = 0;
    for (int i = 1; i <= n; i++) {
        for (int a = 0; a <= total; a++) {
            dp[i][a] = -100000;
            for (int x = k; x <= a; x++)
                dp[i][a] = max(dp[i][a], dp[i - 1][a - x]);
            for (int x = k; x <= total - a; x++)
                dp[i][a] = max(dp[i][a], dp[i - 1][a + x]);
            dp[i][a] += a * (total - a);
        }
    }
    ll ans = 0;
    for (const auto tmp: dp[n])
        ans = max(ans, tmp);
    cout << ans << endl;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int T = 1;
    for (int t = 0; t < T; t++) {
        solve();
    }
    return 0;
}
