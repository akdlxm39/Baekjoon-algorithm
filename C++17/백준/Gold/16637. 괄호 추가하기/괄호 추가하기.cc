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
        char op = expr[i - 1];
        ll nums[2] = {cur, oper(expr[i - 2] - '0', cur, op)};
        char ops[2] = {op, expr[i - 3]};
        dp[di][0] = -INT32_MAX;
        dp[di][1] = INT32_MAX;
        for (int a = 0; a < 2; a++)
            for (int b = 0; b < 2; b++) {
                ll num = oper(dp[di - 1 - a][b], nums[a], ops[a]);
                dp[di][0] = max(dp[di][0], num);
                dp[di][1] = min(dp[di][1], num);
            }
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
