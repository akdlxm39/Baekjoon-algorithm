// https://www.acmicpc.net/problem/16978 수열과 쿼리 22
#include<bits/stdc++.h>
using namespace std;

typedef long long ll;

const int MAX = 100'001;
const ll INF = 100000000000;

int n, m;
ll nums[MAX], tree[MAX];
vector<array<int, 4> > queries;

void update(int idx, ll delta) {
    while (idx <= n) {
        tree[idx] += delta;
        idx += idx & -idx;
    }
}

ll query(int l, int r) {
    ll ret = 0;
    while (0 < r) {
        ret += tree[r];
        r -= r & -r;
    }
    l--;
    while (0 < l) {
        ret -= tree[l];
        l -= l & -l;
    }
    return ret;
}


void solve() {
    cin >> n;
    for (int i = 1; i <= n; ++i) {
        cin >> nums[i];
        update(i, nums[i]);
    }
    cin >> m;
    int q1 = 0, q2 = 0;
    for (int i = 0, q, a, b, c; i < m; ++i) {
        cin >> q >> a >> b;
        if (q == 1) {
            queries.push_back({++q1, -1, a, b});
        } else {
            cin >> c;
            queries.push_back({a, q2++, b, c});
        }
    }
    sort(queries.begin(), queries.end());
    vector<ll> ans(q2);
    for (auto &[_, q, i, j]: queries) {
        if (q == -1) {
            update(i, j - nums[i]);
            nums[i] = j;
        } else {
            ans[q] = query(i, j);
        }
    }
    for (auto &x: ans)
        cout << x << '\n';
}


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int t = 1;
    while (t--) solve();
    return 0;
}
