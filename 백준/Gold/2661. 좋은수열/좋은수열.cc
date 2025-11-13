// https://www.acmicpc.net/problem/2661 좋은 수열
#include<bits/stdc++.h>
using namespace std;

int n;

bool check(const string &cur, int cnt) {
    for (int i = cnt - 1, j = cnt; i >= 0; i -= 2, --j)
        if (cur.find(cur.substr(j), i) == i) return false;
    return true;
}

bool dfs(string &cur, int cnt) {
    if (cnt == n) return true;
    for (auto c: {'1', '2', '3'}) {
        cur.push_back(c);
        if (check(cur, cnt) && dfs(cur, cnt + 1))
            return true;
        cur.pop_back();
    }
    return false;
}

void solve() {
    cin >> n;
    string ans;
    dfs(ans, 0);
    cout << ans << '\n';
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int t = 1;
    while (t--) solve();
    return 0;
}
