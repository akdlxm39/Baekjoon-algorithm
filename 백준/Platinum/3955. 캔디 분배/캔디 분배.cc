#include<bits/stdc++.h>
using namespace std;

typedef long long ll;

const ll MAX = 1000000000LL;
ll k, c;


/**
 * input: a, b \n
 * output: gcd(a,b), x, y \n
 * ax + by = gcd(a,b) \n
 * a = qb + r \n
 * gcd(a,b) == gcd(b,r) \n
 * >> (qb + r)x + by = gcd(b,r)
 * >> b(qx + y) + rx = gcd(b,r)
 */
tuple<ll, ll, ll> extended_uclidean(ll a, ll b) {
    if (b == 0)
        return {a, 1, 0};
    auto [g, x, y] = extended_uclidean(b, a % b);
    return {g, y, x - (a / b) * y};
}

void solve() {
    cin >> k >> c;
    if (c == 1) {
        if (k == MAX)
            cout << "IMPOSSIBLE\n";
        else
            cout << k + 1 << "\n";
        return;
    }
    if (k == 1) {
        cout << "1\n";
        return;
    }
    auto [g, x, y] = extended_uclidean(c, k);
    if (g != 1 || x > 1000000000LL) {
        cout << "IMPOSSIBLE\n";
        return;
    }
    while (x < 0)
        x += k;
    cout << x << '\n';
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int T = 1;
    cin >> T;
    while (T--) solve();
    return 0;
}
