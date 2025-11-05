// https://www.acmicpc.net/problem/2336 굉장한 학생
#include<bits/stdc++.h>
using namespace std;

const int MAX = 500001;
int n, tree[MAX], a_rank[MAX], b_rank[MAX], c_rank[MAX];

void update(int idx, int num) {
    while (idx <= n && tree[idx] > num) {
        tree[idx] = num;
        idx += idx & -idx;
    }
}

int query(int idx) {
    int ret = MAX;
    while (idx > 0) {
        ret = min(ret, tree[idx]);
        idx -= idx & -idx;
    }
    return ret;
}


void solve() {
    cin >> n;
    int ans = n;
    for (int i = 1, x; i <= n; ++i) {
        cin >> x;
        a_rank[i] = x;
    }
    for (int i = 1, x; i <= n; ++i) {
        cin >> x;
        b_rank[x] = i;
    }
    for (int i = 1, x; i <= n; ++i) {
        cin >> x;
        c_rank[x] = i;
    }
    fill(tree, tree + MAX, MAX);
    for (int i = 1; i <= n; ++i) {
        if (query(b_rank[a_rank[i]] - 1) < c_rank[a_rank[i]]) {
            --ans;
        }
        update(b_rank[a_rank[i]], c_rank[a_rank[i]]);
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
