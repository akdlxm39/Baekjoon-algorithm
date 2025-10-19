#include<bits/stdc++.h>
using namespace std;

typedef long long ll;

int r, c, k;
int arr[101][101], counter[101];
int r_size = 3, c_size = 3;

void row_sort() {
    int nxt_c_size = 0;
    for (int i = 1; i <= r_size; i++) {
        memset(counter, 0, sizeof(counter));
        for (int j = 1; j <= c_size; j++) {
            counter[arr[i][j]]++;
        }
        vector<array<int, 2> > sorter;
        for (int n = 1; n <= 100; n++) {
            if (counter[n] != 0)
                sorter.push_back({counter[n], n});
        }
        sort(sorter.begin(), sorter.end());
        int idx = 1;
        for (auto [x, y]: sorter) {
            arr[i][idx++] = y;
            arr[i][idx++] = x;
            if (idx == 101) break;
        }
        nxt_c_size = max(nxt_c_size, idx - 1);
        while (idx <= c_size)
            arr[i][idx++] = 0;
    }
    c_size = nxt_c_size;
}

void col_sort() {
    int nxt_r_size = 0;
    for (int j = 1; j <= c_size; j++) {
        memset(counter, 0, sizeof(counter));
        for (int i = 1; i <= r_size; i++) {
            counter[arr[i][j]]++;
        }
        vector<array<int, 2> > sorter;
        for (int n = 1; n <= 100; n++) {
            if (counter[n] != 0)
                sorter.push_back({counter[n], n});
        }
        sort(sorter.begin(), sorter.end());
        int idx = 1;
        for (auto [x, y]: sorter) {
            arr[idx++][j] = y;
            arr[idx++][j] = x;
            if (idx == 101) break;
        }
        nxt_r_size = max(nxt_r_size, idx - 1);
        while (idx <= r_size)
            arr[idx++][j] = 0;
    }
    r_size = nxt_r_size;
}

void solve() {
    cin >> r >> c >> k;
    for (int i = 1; i <= 3; i++) {
        for (int j = 1; j <= 3; j++) {
            cin >> arr[i][j];
        }
    }
    int t = 0;
    while (arr[r][c] != k && ++t <= 100) {
        if (r_size >= c_size)
            row_sort();
        else
            col_sort();
    }
    cout << (t != 101 ? t : -1) << '\n';
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int T = 1;
    for (int t = 0; t < T; t++) {
        solve();
    }
    return 0;
}
