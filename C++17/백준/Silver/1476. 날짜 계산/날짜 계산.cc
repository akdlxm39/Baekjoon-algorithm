// https://www.acmicpc.net/problem/1476 날짜 계산
#include<bits/stdc++.h>
using namespace std;

typedef long long ll;

const ll MOD[3] = {15, 28, 19}, MOD_ESM = 15 * 28 * 19;
ll nums[3], ans, esm = 1;

tuple<ll, ll, ll> extended_euclidean(ll a, ll b) {
    if (b == 0)
        return {a, 1, 0};
    auto [g, x, y] = extended_euclidean(b, a % b);
    return {g, y, x - a / b * y};
}


void solve() {
    for (int i = 0; i < 3; i++) {
        cin >> nums[i];
        esm *= nums[i];
    }
    for (int i = 0; i < 3; i++) {
        auto [g, x, y] = extended_euclidean(MOD_ESM / MOD[i], MOD[i]);
        while (x < y)
            x += MOD[i] / g;
        ans += MOD_ESM / MOD[i] * x * nums[i];
    }
    cout << (ans - 1) % MOD_ESM + 1 << '\n';
}


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int t = 1;
    while (t--)
        solve();
    return 0;
}
