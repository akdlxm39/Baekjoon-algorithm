// https://www.acmicpc.net/problem/13306 트리
#include<bits/stdc++.h>
using namespace std;

const int MAX = 200'001;

int n, q, parent[MAX], root[MAX];
stack<tuple<int, int, int> > queries;
stack<bool> ans;

int find(int x) {
    if (root[x] != x)
        root[x] = find(root[x]);
    return root[x];
}


void solve() {
    cin >> n >> q;
    parent[1] = root[1] = 1;
    for (int i = 2, j; i <= n; i++) {
        cin >> j;
        parent[i] = j;
        root[i] = i;
    }
    for (int i = 0, a, b, c; i < n + q - 1; i++) {
        cin >> a;
        if (a == 0) {
            cin >> b;
            queries.push({a, b, 0});
        } else {
            cin >> b >> c;
            queries.push({a, b, c});
        }
    }
    while (!queries.empty()) {
        auto [a, b, c] = queries.top();
        queries.pop();
        if (a == 0) {
            root[b] = find(parent[b]);
        } else {
            ans.push(find(b) == find(c));
        }
    }
    while (!ans.empty()) {
        cout << (ans.top() ? "YES" : "NO") << "\n";
        ans.pop();
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
