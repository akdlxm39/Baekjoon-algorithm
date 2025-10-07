#include<bits/stdc++.h>
using namespace std;

typedef long long ll;


/**
 * input: a, b \n
 * output: gcd(a,b), x, y \n
 * ax + by = gcd(a,b) \n
 * a = qb + r \n
 * gcd(a,b) == gcd(b,r) \n
 * >> (qb + r)x + by = gcd(b,r)
 * >> b(qx + y) + rx = gcd(b,r)
 */
tuple<ll, ll, ll> extended_euclidean(ll a, ll b) {
    if (b == 0)
        return {a, 1, 0};
    auto [g, x, y] = extended_euclidean(b, a % b);
    return {g, y, x - (a / b) * y};
}


void solve() {
    ll a, b, c, x1, x2, y1, y2;
    cin >> a >> b >> c;
    cin >> x1 >> x2 >> y1 >> y2;
    if (a > 0LL) {
        ll tmp = x1;
        x1 = -x2;
        x2 = -tmp;
    } else a = -a;
    if (b > 0LL) {
        ll tmp = y1;
        y1 = -y2;
        y2 = -tmp;
    } else b = -b;
    if (a == 0 && b != 0) {
        if (c % b == 0 && y1 <= c / b && c / b <= y2)
            cout << x2 - x1 + 1 << '\n';
        else
            cout << "0\n";
        return;
    }
    if (b == 0 && a != 0) {
        if (c % a == 0 && x1 <= c / a && c / a <= x2)
            cout << y2 - y1 + 1 << '\n';
        else
            cout << "0\n";
        return;
    }
    if (a == 0 & b == 0) {
        if (c == 0)
            cout << (x2 - x1 + 1) * (y2 - y1 + 1) << '\n';
        else
            cout << "0\n";
        return;
    }
    auto [g, x, y] = extended_euclidean(a, b);
    if (c % g != 0) {
        cout << "0\n";
        return;
    }
    a /= g;
    b /= g;
    c /= g;
    x *= c;
    y *= c;
    // cout << "a: " << a << " b: " << b << " c: " << c << '\n';
    // cout << "x1: " << x1 << " x2: " << x2 << " y1: " << y1 << " y2: " << y2 << '\n';
    // cout << "x: " << x << " y: " << y << '\n';
    ll k = (x - x1) / b - (x < x1);
    x -= k * b;
    y += k * a;
    // cout << "k: " << k << " x: " << x << " y: " << y << '\n';
    if (x < x1) {
        x += b;
        y -= a;
    }
    ll ans = 0;
    while (x <= x2 && y1 <= y) {
        if (y <= y2) ans++;
        x += b;
        y -= a;
    }
    cout << ans << '\n';
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int T = 1;
    while (T--) solve();
    return 0;
}
