// https://www.acmicpc.net/problem/7469 K번째 수
#include<bits/stdc++.h>
using namespace std;

typedef long long ll;

const int MAX = 1000000000;

vector<int> tree[400004];
int arr[100001], n, m, smaller;

void show() {
    int i = 1, k = 1;
    int max_depth = int(log2(n - 1)) + 2;
    for (int d = 0; d < max_depth; d++) {
        for (int j = i; j < i + k; j++) {
            if (tree[j].empty()) {
                if (j % 2 == 0) cout << "[ ]";
                continue;
            }
            cout << "[";
            for (int idx = 0; idx < tree[j].size() - 1; idx++)
                cout << tree[j][idx] << "  ";
            cout << tree[j].back() << "]";
        }
        cout << endl;
        i += k;
        k *= 2;
    }
}

void init(int node, int left, int right) {
    if (left == right) {
        tree[node].push_back(arr[left]);
        return;
    }
    int mid = (left + right) / 2;
    init(node * 2, left, mid);
    init(node * 2 + 1, mid + 1, right);
    auto li = tree[node * 2].begin(), ri = tree[node * 2 + 1].begin();
    auto le = tree[node * 2].end(), re = tree[node * 2 + 1].end();
    while (li != le || ri != re) {
        if (ri == re || (li != le && *li < *ri)) tree[node].push_back(*li++);
        else tree[node].push_back(*ri++);
    }
}

bool count(int node, int left, int right, int i, int j, int num) {
    if (right < i || j < left)
        return false;
    if (i <= left && right <= j) {
        auto lb = lower_bound(tree[node].begin(), tree[node].end(), num);
        smaller += int(lb - tree[node].begin());
        return lb != tree[node].end() && *lb == num;
    }
    int mid = (left + right) / 2;
    if (count(node * 2, left, mid, i, j, num)) {
        count(node * 2 + 1, mid + 1, right, i, j, num);
        return true;
    }
    return count(node * 2 + 1, mid + 1, right, i, j, num);
}

int query(int i, int j, int k) {
    int left = -MAX, right = MAX;
    while (left < right) {
        int mid = ((left + right < 0) ? (left + right - 1) / 2 : (left + right) / 2);
        smaller = 0;
        if (count(1, 1, n, i, j, mid) && smaller == k - 1)
            return mid;
        if (smaller < k) left = mid;
        else right = mid;
    }
    return left;
}


void solve() {
    cin >> n >> m;
    for (int i = 1; i <= n; i++) {
        cin >> arr[i];
    }
    init(1, 1, n);
    // show();
    while (m--) {
        int i, j, k;
        cin >> i >> j >> k;
        cout << query(i, j, k) << '\n';
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
