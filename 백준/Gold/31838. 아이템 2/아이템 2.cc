#include<bits/stdc++.h>
using namespace std;

typedef long long ll;
const int MAX = 500005;

int item, n, k;
ll dp[MAX], prefixSum[MAX], max_dp, ans;

void solve() {
    cin >> n >> k;
    ans = 0;
    memset(prefixSum, 0LL, sizeof(prefixSum));
    memset(dp, 0LL, sizeof(dp));
    for (int i = 1; i <= n; i++) {
        cin >> item;
        prefixSum[i] = prefixSum[i - 1] + item;
    }
    for (int i = 1; i <= k; i++) {
        dp[i] = max(dp[i - 1], prefixSum[i]);
        ans = max(ans, dp[i]);
    }
    max_dp = 0LL;
    for (int i = k + 1; i < n; i++) {
        max_dp = max(max_dp, dp[i - k] - prefixSum[i - k]);
        dp[i] = max(dp[i - 1], max_dp + prefixSum[i]);
        ans = max(ans, dp[i]);
    }

    for (int i = n - k; i < n; i++) {
        max_dp = max(max_dp, dp[i] - prefixSum[i]);
        dp[n] = max(dp[n], max_dp + prefixSum[n]);
    }
    ans = max(ans, dp[n]);
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
