// https://www.acmicpc.net/problem/9345 디지털 비디오 디스크(DVDs)
#include<bits/stdc++.h>
using namespace std;

const int MAX = 100'001;


int n, k;
int tree[MAX * 4], dvds[MAX];
int prefix_sum[MAX];

void make_prefix_sum() {
    for (int i = 1; i < MAX; i++)
        prefix_sum[i] = prefix_sum[i - 1] + i;
}

void init(int node, int left, int right) {
    if (left == right) {
        tree[node] = dvds[left] = left;
        return;
    }
    int mid = (left + right) / 2;
    init(node * 2, left, mid);
    init(node * 2 + 1, mid + 1, right);
    tree[node] = tree[node * 2] + tree[node * 2 + 1];
}

void update(int node, int left, int right, int idx, int delta) {
    tree[node] += delta;
    if (left == right) return;
    int mid = (left + right) / 2;
    if (idx <= mid)
        update(node * 2, left, mid, idx, delta);
    else
        update(node * 2 + 1, mid + 1, right, idx, delta);
}

int query(int node, int left, int right, int start, int end) {
    if (right < start || end < left) return 0;
    if (start <= left && right <= end) return tree[node];
    int mid = (left + right) / 2;
    return query(node * 2, left, mid, start, end) +
           query(node * 2 + 1, mid + 1, right, start, end);
}


void solve() {
    cin >> n >> k;
    init(1, 0, n - 1);
    for (int i = 0, q, a, b; i < k; i++) {
        cin >> q >> a >> b;
        if (q == 0) {
            int delta = dvds[b] - dvds[a];
            update(1, 0, n - 1, a, delta);
            update(1, 0, n - 1, b, -delta);
            swap(dvds[a], dvds[b]);
        } else {
            int true_sum = a != 0 ? prefix_sum[b] - prefix_sum[a - 1] : prefix_sum[b];
            if (true_sum == query(1, 0, n - 1, a, b)) {
                int j = a;
                for (; j <= b; ++j) {
                    if (dvds[j] < a || b < dvds[j]) {
                        cout << "NO\n";
                        break;
                    }
                }
                if (j > b) cout << "YES\n";
            } else
                cout << "NO\n";
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    make_prefix_sum();
    int t = 1;
    cin >> t;
    while (t--)
        solve();
    return 0;
}
