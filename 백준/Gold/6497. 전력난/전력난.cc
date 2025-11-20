// https://www.acmicpc.net/problem/6497 전력난
#include<bits/stdc++.h>
using namespace std;

const int MAX = 200001;

int n, m, root[MAX], ans;
vector<array<int, 3> > edges;

int find(int x) {
    if (x != root[x]) root[x] = find(root[x]);
    return root[x];
}

bool union_(int a, int b) {
    a = find(a);
    b = find(b);
    if (a == b) return false;
    root[a] = b;
    return true;
}


bool solve() {
    cin >> m >> n;
    if (n == 0 && m == 0) return false;
    edges.resize(n);
    ans = 0;
    for (int i = 0; i < n; ++i)
        root[i] = i;
    for (auto &[z, x, y]: edges) {
        cin >> x >> y >> z;
        ans += z;
    }
    sort(edges.begin(), edges.end());
    for (auto &[z, x, y]: edges)
        if (union_(x, y))
            ans -= z;
    cout << ans << '\n';

    return true;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    // int t = 1;
    // while (t--) solve();
    while (solve()) {
    }
    return 0;
}
