#include<bits/stdc++.h>

using namespace std;

vector<int> tree[400001];
int n, m, x;

void init(int node, int left, int right) {
    if (left == right) {
        cin >> x;
        tree[node].push_back(x);
        return;
    }
    int mid = (left + right) / 2;
    init(node * 2, left, mid);
    init(node * 2 + 1, mid + 1, right);
    auto li = tree[node * 2].begin(), le = tree[node * 2].end();
    auto ri = tree[node * 2 + 1].begin(), re = tree[node * 2 + 1].end();
    while (li != le || ri != re) {
        if (ri == re || (li != le && *li < *ri))
            tree[node].push_back(*li++);
        else
            tree[node].push_back(*ri++);
    }
}

int query(int node, int left, int right, int start, int end, int num) {
    if (right < start || end < left)
        return 0;
    if (start <= left && right <= end) {
        auto ub = upper_bound(tree[node].begin(), tree[node].end(), num);
        return tree[node].end() - ub;
    }
    int mid = (left + right) / 2;
    return query(node * 2, left, mid, start, end, num) +
           query(node * 2 + 1, mid + 1, right, start, end, num);
}

void solve() {
    cin >> n;
    init(1, 1, n);
    cin >> m;
    int ans = 0, a, b, c;
    while (m--) {
        cin >> a >> b >> c;
        a ^= ans;
        b ^= ans;
        c ^= ans;
        ans = query(1, 1, n, a, b, c);
        cout << ans << '\n';
    }
}


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int t = 1;
    while (t--)
        solve();
    return 0;
}
