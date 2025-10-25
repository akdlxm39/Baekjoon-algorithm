// https://www.acmicpc.net/problem/9345 디지털 비디오 디스크(DVDs)
#include<bits/stdc++.h>
using namespace std;

const int MAX = 100'001;


int n, k;
int min_tree[MAX * 4], max_tree[MAX * 4], dvds[MAX];


void init(int node, int left, int right) {
    if (left == right) {
        min_tree[node] = max_tree[node] = dvds[left] = left;
        return;
    }
    int mid = (left + right) / 2;
    init(node * 2, left, mid);
    init(node * 2 + 1, mid + 1, right);
    min_tree[node] = min(min_tree[node * 2], min_tree[node * 2 + 1]);
    max_tree[node] = max(max_tree[node * 2], max_tree[node * 2 + 1]);
}

void update(int node, int left, int right, int idx, int key) {
    if (left == right) {
        min_tree[node] = max_tree[node] = key;
        return;
    }
    int mid = (left + right) / 2;
    if (idx <= mid)
        update(node * 2, left, mid, idx, key);
    else
        update(node * 2 + 1, mid + 1, right, idx, key);
    min_tree[node] = min(min_tree[node * 2], min_tree[node * 2 + 1]);
    max_tree[node] = max(max_tree[node * 2], max_tree[node * 2 + 1]);
}

tuple<int, int> query(int node, int left, int right, int start, int end) {
    if (right < start || end < left) return {MAX, 0};
    if (start <= left && right <= end) return {min_tree[node], max_tree[node]};
    int mid = (left + right) / 2;
    auto [min_l, max_l] = query(node * 2, left, mid, start, end);
    auto [min_r, max_r] = query(node * 2 + 1, mid + 1, right, start, end);
    return {min(min_l, min_r), max(max_l, max_r)};
}


void solve() {
    cin >> n >> k;
    init(1, 0, n - 1);
    for (int i = 0, q, a, b; i < k; i++) {
        cin >> q >> a >> b;
        if (q == 0) {
            update(1, 0, n - 1, a, dvds[b]);
            update(1, 0, n - 1, b, dvds[a]);
            swap(dvds[a], dvds[b]);
        } else {
            auto [l, r] = query(1, 0, n - 1, a, b);
            cout << (l == a && r == b ? "YES\n" : "NO\n");
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int t = 1;
    cin >> t;
    while (t--)
        solve();
    return 0;
}
