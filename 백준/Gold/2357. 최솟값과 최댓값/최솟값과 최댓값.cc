// https://www.acmicpc.net/problem/2357 최솟값과 최댓값
#include<bits/stdc++.h>
using namespace std;

const int MIN = 0, MAX = 1'000'000'001;

int n, m, min_tree[400000], max_tree[400000];

void init(int node, int left, int right) {
    if (left == right) {
        cin >> min_tree[node];
        max_tree[node] = min_tree[node];
        return;
    }
    int mid = (left + right) / 2;
    init(node * 2, left, mid);
    init(node * 2 + 1, mid + 1, right);
    min_tree[node] = min(min_tree[node * 2], min_tree[node * 2 + 1]);
    max_tree[node] = max(max_tree[node * 2], max_tree[node * 2 + 1]);
}

array<int, 2> query(int node, int left, int right, int start, int end) {
    if (right < start || end < left)
        return {MAX, MIN};
    if (start <= left && right <= end)
        return {min_tree[node], max_tree[node]};
    int mid = (left + right) / 2;
    auto [left_min, left_max] = query(node * 2, left, mid, start, end);
    auto [right_min, right_max] = query(node * 2 + 1, mid + 1, right, start, end);
    return {min(left_min, right_min), max(left_max, right_max)};
}

void solve() {
    cin >> n >> m;
    init(1, 1, n);
    while (m--) {
        int a, b;
        cin >> a >> b;
        auto [min_ans, max_ans] = query(1, 1, n, a, b);
        cout << min_ans << ' ' << max_ans << '\n';
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int t = 1;
    while (t--) solve();
    return 0;
}
