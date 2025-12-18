// https://www.acmicpc.net/problem/1647 도시 분할 계획
#include<bits/stdc++.h>
using namespace std;

int n, m, root[100'001], ans;
vector<array<int, 3> > roads;

int find(int a) {
    return root[a] == a ? a : root[a] = find(root[a]);
}

bool union_(int a, int b) {
    a = find(a), b = find(b);
    if (a == b) return false;
    if (a > b) root[a] = b;
    else root[b] = a;
    return true;
}

void solve() {
    cin >> n >> m;
    if (n == 2) {
        cout << "0\n";
        return;
    }
    roads.resize(m);
    for (auto &[a, b, c]: roads)
        cin >> a >> b >> c;
    sort(roads.begin(), roads.end(),
         [](array<int, 3> l, array<int, 3> r) { return l[2] < r[2]; });
    ans = 0;
    for (int i = 1; i <= n; ++i)
        root[i] = i;
    for (auto &[a, b, c]: roads) {
        if (union_(a, b)) {
            ans += c;
            if (--n == 2) break;
        }
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
