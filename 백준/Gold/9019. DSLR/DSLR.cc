// https://www.acmicpc.net/problem/9019 DSLR
#include<bits/stdc++.h>
using namespace std;

struct funcTable {
    char func_name;

    int (*func)(int);

    funcTable(char func_name, int (*func)(int)) : func_name(func_name), func(func) { ; }
};

const funcTable DSLR[4] = {
    funcTable('D', [](int x) { return 2 * x % 10000; }),
    funcTable('S', [](int x) { return x != 0 ? x - 1 : 9999; }),
    funcTable('L', [](int x) { return x / 1000 + x % 1000 * 10; }),
    funcTable('R', [](int x) { return x % 10 * 1000 + x / 10; }),
};

int a, b;
bool visited[10000];

void solve() {
    cin >> a >> b;
    memset(visited, false, sizeof(visited));
    queue<tuple<int, string> > q;
    q.emplace(a, "");
    visited[a] = true;
    while (!q.empty()) {
        auto [cur, cur_str] = q.front();
        q.pop();
        for (auto &[c, f]: DSLR) {
            int nxt = f(cur);
            if (nxt == b) {
                cout << cur_str + c << '\n';
                return;
            }
            if (visited[nxt]) continue;
            visited[nxt] = true;
            q.emplace(nxt, cur_str + c);
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int t = 1;
    cin >> t;
    while (t--) solve();
    return 0;
}
