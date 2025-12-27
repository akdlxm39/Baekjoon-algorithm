// https://www.acmicpc.net/problem/7579 앱
#include<bits/stdc++.h>
using namespace std;

struct app {
    int byte;
    int cost;
};

int n, m, bytes, costs, ans = int(1e9);
vector<app> apps;
vector<int> dp;

void solve() {
    cin >> n >> m;
    apps.resize(n);
    for (int i = 0; i < n; ++i) {
        cin >> apps[i].byte;
        bytes += apps[i].byte;
    }
    for (int i = 0; i < n; ++i) {
        cin >> apps[i].cost;
        costs += apps[i].cost;
    }
    dp.resize(costs + 1, 0);
    for (auto [byte, cost]: apps) {
        for (int i = costs; i >= cost; --i) {
            dp[i] = max(dp[i], dp[i - cost] + byte);
            if (dp[i] >= m && ans > i)
                ans = i;
        }
    }
    cout << ans << ' ';
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int t = 1;
    while (t--) solve();
    return 0;
}
