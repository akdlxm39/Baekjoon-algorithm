// https://www.acmicpc.net/problem/2166 다각형의 면적
#include<bits/stdc++.h>
using namespace std;

int n;
vector<array<double, 2> > points;

void solve() {
    cin >> n;
    points.resize(n);
    for (auto &[x, y]: points)
        cin >> x >> y;
    double ans = 0.0;
    for (int cur = 0, prev = n - 1; cur < n; prev = cur++) {
        ans += (points[prev][0] + points[cur][0]) * (points[prev][1] - points[cur][1]);
    }
    cout << abs(ans) / 2 << '\n';
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout << fixed;
    cout.precision(1);
    int t = 1;
    while (t--) solve();
    return 0;
}
