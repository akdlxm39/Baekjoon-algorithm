// https://testcase.ac/problems/12852 1로 만들기 2
#include<bits/stdc++.h>
using namespace std;

typedef long long ll;
const int MAX = 1000001;

int dp[MAX], n;

void solve() {
    memset(dp, -1, sizeof(dp));
    cin >> n;
    queue<int> q;
    q.push(1);
    dp[1] = 0;
    while (!q.empty()) {
        int cur = q.front();
        q.pop();
        if (cur * 3 <= n && dp[cur * 3] == -1) {
            dp[cur * 3] = cur;
            q.push(cur * 3);
        }
        if (cur * 2 <= n && dp[cur * 2] == -1) {
            dp[cur * 2] = cur;
            q.push(cur * 2);
        }
        if (cur < n && dp[cur + 1] == -1) {
            dp[cur + 1] = cur;
            q.push(cur + 1);
        }
        if (dp[n] != -1)
            break;
    }
    vector<int> ans;
    int cur = n, cnt = -1;
    while (cur != 0) {
        ans.push_back(cur);
        cur = dp[cur];
        cnt++;
    }
    cout << cnt << '\n';
    for (auto x: ans)
        cout << x << ' ';
    cout << '\n';
}

int dfs(int n) {
    if (n <= 1)
        return 0;
    int a = dfs(n / 3) + n % 3;
    int b = dfs(n / 2) + n % 2;
    if (a <= b) {
        dp[n] = n / 3;
        return a + 1;
    } else {
        dp[n] = n / 2;
        return b + 1;
    }
}

void solve2() {
    memset(dp, -1, sizeof(dp));
    cin >> n;
    int cnt = dfs(n);
    dp[1] = 0;
    cout << cnt << '\n';
    int nxt = dp[n];
    while (n) {
        cout << n << ' ';
        if (nxt * 3 != n && nxt * 2 != n) {
            n--;
            continue;
        }
        n = nxt;
        nxt = dp[n];
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int T = 1;
    for (int t = 0; t < T; t++) {
        solve2();
    }
    return 0;
}
