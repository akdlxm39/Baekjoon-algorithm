// https://www.acmicpc.net/problem/2056 작업
#include<bits/stdc++.h>
using namespace std;

const int MAX = 10001;

int n, cost[MAX], ans;


void solve() {
    cin >> n;
    for (int i = 1, t, m; i <= n; ++i) {
        cin >> t >> m;
        while (m--) {
            int j;
            cin >> j;
            cost[i] = max(cost[i], cost[j]);
        }
        cost[i] += t;
        ans = max(ans, cost[i]);
    }
    cout << ans << '\n';
}


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int t = 1;
    while (t--) solve();
    return 0;
}
