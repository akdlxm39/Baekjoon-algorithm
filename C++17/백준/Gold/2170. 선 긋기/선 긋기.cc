// https://www.acmicpc.net/problem/2170 선 긋기
#include<bits/stdc++.h>
using namespace std;

vector<array<int, 2> > lines;
int n;

void solve() {
    cin >> n;
    lines.resize(n);

    for (auto &line: lines)
        cin >> line[0] >> line[1];
    sort(lines.begin(), lines.end());
    int cur = -1'000'000'000, ans = 0;
    for (auto &[l, r]: lines) {
        if (l <= cur && cur < r) {
            ans += r - cur;
        } else if (cur < l) {
            ans += r - l;
        }
        cur = max(cur, r);
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
