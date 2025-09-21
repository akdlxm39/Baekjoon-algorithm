// https://www.acmicpc.net/problem/2011 암호코드
#include<bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;

#define FAST_IO ios_base::sync_with_stdio(0);cin.tie(NULL);
#define MOD 1000000

void solve() {
    string s;
    cin >> s;
    if (s[0] == '0') {
        cout << 0 << endl;
        return;
    }
    vector<int> dp(s.size() + 1, 0);
    dp[0] = dp[1] = 1;
    for (int i = 1; i < s.size(); i++) {
        if (s[i] == '0') {
            if (s[i - 1] == '1' || s[i - 1] == '2') {
                dp[i + 1] += dp[i - 1];
            } else {
                cout << 0 << endl;
                return;
            }
        } else {
            dp[i + 1] += dp[i];
            if (s[i - 1] == '1') {
                dp[i + 1] += dp[i - 1];
            } else if (s[i - 1] == '2' && '1' <= s[i] && s[i] <= '6') {
                dp[i + 1] += dp[i - 1];
            }
        }
        dp[i + 1] %= MOD;
    }
    cout << dp[s.size()] << endl;
}

int main() {
    FAST_IO
    int T = 1;
    for (int i = 0; i < T; i++) {
        solve();
    }
    return 0;
}
