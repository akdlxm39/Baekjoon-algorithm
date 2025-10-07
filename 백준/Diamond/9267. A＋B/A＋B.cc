#include<bits/stdc++.h>
using namespace std;

// typedef long long ll;
#define ll __int128
#define check_print(a, b) if (a) {cout << (b?"YES\n":"NO\n"); return;}

ll a, b, s;
ll gcd(ll a, ll b) { return (b ? gcd(b, a % b) : a); }

tuple<ll, ll, ll> extended_euclidean(ll a, ll b) {
    if (b == 0)
        return {a, 1, 0};
    auto [g, x, y] = extended_euclidean(b, a % b);
    return {g, y, x - (a / b * y)};
}


void solve() {
    long long aa, bb, ss;
    cin >> aa >> bb >> ss;
    a = aa;
    b = bb;
    s = ss;
    check_print(a==0&&b==0, s==0)
    check_print(a==0, s%b==0)
    check_print(b==0, s%a==0)
    check_print(a==s||b==s, true)
    auto [g, x, y] = extended_euclidean(a, b);
    check_print(s%g!=0, false)
    a /= g;
    b /= g;
    s /= g;
    x *= s;
    y *= s;
    if (x < y) {
        swap(a, b);
        swap(x, y);
    }
    ll k = -y / a + 1;
    x -= k * b;
    y += k * a;
    while (x > 0) {
        check_print(gcd(x,y)==1, true)
        x -= b;
        y += a;
    }
    check_print(true, false)
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int T = 1;
    while (T--) solve();
    return 0;
}
