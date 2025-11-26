// https://www.acmicpc.net/problem/12899 데이터 구조
#include<bits/stdc++.h>
using namespace std;

struct SegmentTree {
    vector<int> tree;

    explicit SegmentTree() {
        tree = vector<int>(4'200'000, 0);
    }

    void append(int x) {
        append(1, 1, 2'000'000, x);
    }

    void append(int node, int left, int right, int num) {
        ++tree[node];
        if (left == right) return;
        int mid = (left + right) / 2;
        if (left <= num && num <= mid)
            append(node * 2, left, mid, num);
        else
            append(node * 2 + 1, mid + 1, right, num);
    }

    int pop(int x) {
        return pop(1, 1, 2'000'000, x);
    }

    int pop(int node, int left, int right, int idx) {
        --tree[node];
        if (left == right)
            return left;
        if (idx <= tree[node * 2])
            return pop(node * 2, left, (left + right) / 2, idx);
        else
            return pop(node * 2 + 1, (left + right) / 2 + 1, right, idx - tree[node * 2]);
    }
} segment_tree;

int n;

void solve() {
    cin >> n;
    int t, x;
    while (n--) {
        cin >> t >> x;
        if (t == 1)
            segment_tree.append(x);
        else
            cout << segment_tree.pop(x) << '\n';
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int t = 1;
    while (t--) solve();
    return 0;
}
