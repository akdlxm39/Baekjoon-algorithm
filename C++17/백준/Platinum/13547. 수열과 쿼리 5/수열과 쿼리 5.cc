// https://www.acmicpc.net/problem/13547 수열과 쿼리 5
#include<bits/stdc++.h>
using namespace std;

int n, m, rtn;
vector<int> arr, ans;
vector<array<int, 3> > queries;

bool cmp(const array<int, 3> &a, const array<int, 3> &b) {
    auto &[_, ai, aj] = a;
    auto &[__, bi, bj] = b;
    int ain = ai / rtn, bin = bi / rtn;
    if (ain == bin) return aj < bj;
    return ain < bin;
}

void solve() {
    cin >> n;
    rtn = int(sqrt(n));
    arr.resize(n + 1);
    for (int i = 1; i <= n; ++i)
        cin >> arr[i];
    cin >> m;
    queries.resize(m);
    ans.resize(m);
    int qid = 0;
    for (auto &[id, i, j]: queries) {
        cin >> i >> j;
        id = qid++;
    }
    sort(queries.begin(), queries.end(), cmp);
    int s = 1, e = 1, cnt = 1;
    unordered_map<int, int> dict;
    dict[arr[s]] = 1;
    for (auto &[id, i, j]: queries) {
        while (s < i)
            if (--dict[arr[s++]] == 0) cnt--;
        while (s > i)
            if (++dict[arr[--s]] == 1) cnt++;
        while (e < j)
            if (++dict[arr[++e]] == 1) cnt++;
        while (e > j)
            if (--dict[arr[e--]] == 0) cnt--;
        ans[id] = cnt;
    }
    for (auto &a: ans)
        cout << a << '\n';
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int t = 1;
    while (t--) solve();
    return 0;
}
