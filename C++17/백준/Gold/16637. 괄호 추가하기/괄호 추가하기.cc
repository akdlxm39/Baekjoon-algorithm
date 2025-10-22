// https://www.acmicpc.net/problem/16637 괄호 추가하기
#include<bits/stdc++.h>
using namespace std;

typedef long long ll;

ll dp[13][2], n;
string expr;

ll oper(ll a, ll b, char op) {
    if (op == '+') return a + b;
    if (op == '-') return a - b;
    if (op == '*') return a * b;
}

void solve() {
    cin >> n >> expr;
    n += 4;
    expr = "0+0+" + expr;
    for (int i = 4, di = 2; i < n; i += 2, di++) {
        ll cur = expr[i] - '0';
        char op1 = expr[i - 1];
        ll prev = expr[i - 2] - '0';
        char op2 = expr[i - 3];
        ll cur_prev = oper(prev, cur, op1);
        dp[di][0] = max(max(oper(dp[di - 1][0], cur, op1), oper(dp[di - 1][1], cur, op1)),
                        max(oper(dp[di - 2][0], cur_prev, op2), oper(dp[di - 2][1], cur_prev, op2)));
        dp[di][1] = min(min(oper(dp[di - 1][0], cur, op1), oper(dp[di - 1][1], cur, op1)),
                        min(oper(dp[di - 2][0], cur_prev, op2), oper(dp[di - 2][1], cur_prev, op2)));
    }
    // for (auto x: dp)
    //     cout << x[0] << ' ' << x[1] << endl;
    cout << dp[n / 2][0] << '\n';
}


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int t = 1;
    while (t--)
        solve();
    return 0;
}
