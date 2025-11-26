// https://www.acmicpc.net/problem/12899 데이터 구조
#include<bits/stdc++.h>
using namespace std;

struct FenwickTree {
    vector<int> tree;
    int size;

    explicit FenwickTree(int size) : tree(size + 1), size(size) { ; }

    void append(int num, int delta = 1) {
        for (; num <= size; num += num & -num)
            tree[num] += delta;
    }

    int pop(int kth) {
        int cur = 0;
        for (int x = 20; x >= 0; --x) {
            int nxt = cur + (1 << x);
            if (nxt <= size && tree[nxt] < kth) {
                kth -= tree[nxt];
                cur = nxt;
            }
        }
        append(++cur, -1);
        return cur;
    }
} fenwick_tree(2'000'000);

int n;

void solve() {
    cin >> n;
    int t, x;
    while (n--) {
        cin >> t >> x;
        if (t == 1)
            fenwick_tree.append(x);
        else
            cout << fenwick_tree.pop(x) << '\n';
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int t = 1;
    while (t--) solve();
    return 0;
}
