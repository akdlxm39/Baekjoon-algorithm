// https://www.acmicpc.net/problem/6064 카잉 달력
#include<bits/stdc++.h>

using namespace std;

typedef long long ll;


ll euclidean(ll a, ll b) { return b == 0 ? a : euclidean(b, a % b); }

tuple<ll, ll, ll> extended_euclidean(ll a, ll b) {
    if (b == 0)
        return {a, 1, 0};
    auto [g, x, y] = extended_euclidean(b, a % b);
    return {g, y, x - a / b * y};
}

void solve() {
    ll m, n, a, b, ans;
    cin >> m >> n >> a >> b;
    auto [g, x, y] = extended_euclidean(m, n);
    if ((b - a) % g != 0) {
        cout << "-1\n";
        return;
    }
    x *= (b - a) / g;
    ans = (m * x + a) % (m * n / g);
    cout << (ans <= 0 ? ans + m * n / g : ans) << '\n';
}


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int t = 1;
    cin >> t;
    while (t--)
        solve();
    return 0;
}
