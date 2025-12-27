// https://www.acmicpc.net/problem/2239 스도쿠
#include<bits/stdc++.h>
using namespace std;

bool row[10][9], col[10][9], sqr[10][9];
int cnt[10];
vector<string> sdk(9);
vector<int> blank;

void toggle(int cur, int i, int j, bool b) {
    row[cur][i] = b;
    col[cur][j] = b;
    sqr[cur][i / 3 * 3 + j / 3] = b;
    cnt[cur] += b ? 1 : -1;
}

bool can_put(int cur, int i, int j) {
    return !row[cur][i] && !col[cur][j] && !sqr[cur][i / 3 * 3 + j / 3];
}

void dfs(int cur) {
    if (cur == blank.size()) {
        for (auto s: sdk)
            cout << s << '\n';
        exit(0);
    }
    int i = blank[cur] / 9, j = blank[cur] % 9;
    for (int x = 1; x <= 9; ++x) {
        if (can_put(x, i, j)) {
            sdk[i][j] = '0' + x;
            toggle(x, i, j, true);
            dfs(cur + 1);
            sdk[i][j] = '0';
            toggle(x, i, j, false);
        }
    }
}

void solve() {
    for (int i = 0; i < 9; ++i)
        cin >> sdk[i];
    for (int i = 0; i < 9; ++i) {
        for (int j = 0; j < 9; ++j) {
            int cur = sdk[i][j] - '0';
            if (cur != 0)
                toggle(cur, i, j, true);
            else
                blank.push_back(i * 9 + j);
        }
    }
    dfs(0);
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int t = 1;
    while (t--) solve();
    return 0;
}
