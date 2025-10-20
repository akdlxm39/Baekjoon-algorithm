// https://www.acmicpc.net/problem/23062 백남이의 여행 준비의 준비
#include<bits/stdc++.h>

using namespace std;

typedef __int128 ll;

tuple<ll, ll, ll> extended_euclidean(ll a, ll b) {
    if (b == 0)
        return {a, 1, 0};
    auto [g, x, y] = extended_euclidean(b, a % b);
    return {g, y, x - a / b * y};
}

tuple<ll, ll> crt(ll a, ll b, ll mod_a, ll mod_b) {
    auto [g, x, y] = extended_euclidean(mod_a, mod_b);
    ll q = (b - a) / g;
    ll r = (b - a) % g;
    if (r != 0)
        return {-1, -1};
    ll mod_ab = mod_a * mod_b / g;
    ll ab = (mod_a * x * q + a) % mod_ab;
    if (ab <= 0) ab += mod_ab;
    return {ab, mod_ab};
}

void solve() {
    long long mod_aa, mod_bb, mod_cc, aa, bb, cc;
    cin >> mod_aa >> mod_bb >> mod_cc >> aa >> bb >> cc;
    ll mod_a = mod_aa, mod_b = mod_bb, mod_c = mod_cc, a = aa, b = bb, c = cc;
    auto [ab, mod_ab] = crt(a, b, mod_a, mod_b);
    if (ab == -1) {
        cout << "-1\n";
        return;
    }
    auto [abc, _] = crt(ab, c, mod_ab, mod_c);
    cout << (long long) abc << '\n';
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
