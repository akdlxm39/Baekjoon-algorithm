// https://www.acmicpc.net/problem/12920 평범한 배낭 2
#include<bits/stdc++.h>
using namespace std;

const int MAX = 10001;
int n, m, dp[MAX];
vector<array<int, 2> > items;


bool cmp(array<int, 2> &l, array<int, 2> &r) {
    return l[1] * r[0] > r[1] * l[0];
}

void solve() {
    cin >> n >> m;
    items.resize(n);
    for (int i = 0; i < n; ++i) {
        int v, c, k;
        cin >> v >> c >> k;
        int x = 1;
        while (x < k) {
            items.push_back({v * x, c * x});
            k -= x;
            x *= 2;
        }
        items.push_back({v * k, c * k});
    }
    sort(items.begin(), items.end(), cmp);
    for (auto &[v, c]: items) {
        for (int i = m; i >= v; --i)
            dp[i] = max(dp[i], dp[i - v] + c);
    }
    cout << dp[m] << '\n';
}


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int t = 1;
    while (t--) solve();
    return 0;
}
