// https://www.acmicpc.net/problem/2251 물통
#include<bits/stdc++.h>
using namespace std;

const int MAX = 201;
bool visited[MAX][MAX];
int cups[3];
set<int> ans;

array<int, 3> pour(const array<int, 3> cur, int s, int e) {
    array<int, 3> nxt = {0};
    nxt[e] = min(cups[e], cur[s] + cur[e]);
    nxt[s] = cur[s] + cur[e] - nxt[e];
    nxt[3 - s - e] = cur[3 - s - e];
    return nxt;
}

void solve() {
    for (int i = 0; i < 3; ++i)
        cin >> cups[i];
    queue<array<int, 3> > q;
    q.push({0, 0, cups[2]});
    visited[0][0] = true;
    while (!q.empty()) {
        array<int, 3> cur = q.front();
        q.pop();
        if (cur[0] == 0)
            ans.insert(cur[2]);
        for (int i = 0; i < 3; ++i) {
            if (cur[i] == 0) continue;
            for (int j = 0; j < 3; ++j) {
                if (i == j) continue;
                auto nxt = pour(cur, i, j);
                if (!visited[nxt[0]][nxt[1]]) {
                    q.push(nxt);
                    visited[nxt[0]][nxt[1]] = true;
                }
            }
        }
    }
    for (auto x: ans) {
        cout << x << ' ';
    }
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
