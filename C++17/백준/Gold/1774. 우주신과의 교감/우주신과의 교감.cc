// https://www.acmicpc.net/problem/1774 우주신과의 교감
#include<bits/stdc++.h>
using namespace std;

typedef long long ll;
const int MAX = 1001;

int n, m, root[MAX], rest;
array<ll, 2> member[MAX];
vector<tuple<double, int, int> > adj;
double ans = 0.0;

double dist(const array<ll, 2> &a, const array<ll, 2> &b) {
    return sqrt((b[0] - a[0]) * (b[0] - a[0]) + (b[1] - a[1]) * (b[1] - a[1]));
}

int find(int x) {
    if (root[x] != x) root[x] = find(root[x]);
    return root[x];
}

bool union_(int a, int b) {
    int ra = find(a), rb = find(b);
    if (ra == rb) return false;
    root[ra] = rb;
    return true;
}

void solve() {
    cin >> n >> m;
    for (int i = 1; i <= n; ++i)
        cin >> member[i][0] >> member[i][1];

    rest = n - 1;
    for (int i = 1; i <= n; ++i)
        root[i] = i;
    while (m--) {
        int a, b;
        cin >> a >> b;
        rest -= union_(a, b);
    }
    if (rest != 0) {
        for (int i = 1; i <= n; ++i)
            for (int j = 1; j < i; ++j)
                adj.emplace_back(dist(member[i], member[j]), i, j);
        sort(adj.begin(), adj.end());
        for (auto &[d, a, b]: adj) {
            if (union_(a, b)) {
                ans += d;
                if (--rest == 0) break;
            }
        }
    }
    cout << ans << '\n';
}


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout << fixed;
    cout.precision(2);
    int t = 1;
    while (t--) solve();
    return 0;
}
