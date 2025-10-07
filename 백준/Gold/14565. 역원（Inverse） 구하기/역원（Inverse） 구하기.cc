#include<bits/stdc++.h>
using namespace std;

typedef long long ll;

ll a0, n;

/**
 * input: a, b \n
 * output: gcd(a,b), x, y
 * ax + by = gcd(a,b) \n
 * a = qb + r \n
 * gcd(a,b) == gcd(b,r) \n
 */
tuple<ll, ll, ll> extended_uclidean(ll a, ll b) {
    if (b == 0)
        return {a, 1, 0};
    auto [g, x, y] = extended_uclidean(b, a % b);
    return {g, y, x - (a / b) * y};
}


void solve() {
    cin >> n >> a0;
    cout << n - a0 << ' ';
    auto [g, x, y] = extended_uclidean(a0, n);
    if (g != 1LL) cout << "-1\n";
    else {
        while (x < 0LL) {
            x += n / g;
        }
        cout << x << '\n';
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int T = 1;
    while (T--) solve();
    return 0;
}
