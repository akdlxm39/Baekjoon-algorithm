// https://www.acmicpc.net/problem/1476 날짜 계산
#include<bits/stdc++.h>
using namespace std;

typedef long long ll;

const ll MOD[3] = {15, 28, 19}, MOD_ESM = 15 * 28 * 19;
ll a, ans;

tuple<ll, ll, ll> extended_euclidean(ll a, ll b) {
    if (b == 0)
        return {a, 1, 0};
    auto [g, x, y] = extended_euclidean(b, a % b);
    return {g, y, x - a / b * y};
}


void solve() {
    for (int i = 0; i < 3; i++) {
        cin >> a;
        auto [g, x, y] = extended_euclidean(MOD_ESM / MOD[i], MOD[i]);
        ans += MOD_ESM / MOD[i] * x * a;
    }
    ans = ans - (ans / MOD_ESM - 1) * MOD_ESM;
    ans = (ans - 1) % MOD_ESM + 1;
    cout << ans << '\n';
}


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int t = 1;
    while (t--)
        solve();
    return 0;
}
