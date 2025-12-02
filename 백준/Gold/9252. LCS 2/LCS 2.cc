// https://www.acmicpc.net/problem/9252 LCS 2
#include<bits/stdc++.h>
using namespace std;

string a, b;
vector<vector<int> > dp;

void solve() {
    cin >> a >> b;
    dp.resize(a.size() + 1, vector(b.size() + 1, 0));
    for (int i = 0; i < a.size(); ++i) {
        for (int j = 0; j < b.size(); ++j) {
            if (a[i] == b[j])
                dp[i + 1][j + 1] = dp[i][j] + 1;
            else
                dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1]);
        }
    }
    int k = dp[a.size()][b.size()];
    cout << k << '\n';
    if (k) {
        vector<char> ans(k);
        int i = a.size(), j = b.size();
        while (i != 0 && j != 0) {
            if (dp[i][j] == dp[i - 1][j])
                --i;
            else if (dp[i][j] == dp[i][j - 1])
                --j;
            else
                ans[dp[i--][j--] - 1] = a[i - 1];
        }
        for (auto &c: ans)
            cout << c;
        cout << '\n';
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int t = 1;
    while (t--) solve();
    return 0;
}
