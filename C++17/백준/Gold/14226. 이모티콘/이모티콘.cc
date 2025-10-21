// https://www.acmicpc.net/problem/14226 이모티콘
#include<bits/stdc++.h>

using namespace std;

const int MAX = 2001;
int n;
bool visited[MAX][MAX];

void solve() {
    cin >> n;
    queue<tuple<int, int, int> > q; // length, paste, count
    q.push({1, 0, 1});
    visited[1][0] = true;
    while (!q.empty()) {
        auto [cur, paste, count] = q.front();
        q.pop();
        if (cur > 1 && !visited[cur - 1][paste]) {
            if (cur - 1 == n) {
                cout << count << '\n';
                return;
            }
            visited[cur - 1][paste] = true;
            q.push({cur - 1, paste, count + 1});
        }
        if (cur + paste < MAX && !visited[cur + paste][paste]) {
            if (cur + paste == n) {
                cout << count << '\n';
                return;
            }
            visited[cur + paste][paste] = true;
            q.push({cur + paste, paste, count + 1});
        }
        if (!visited[cur][cur]) {
            visited[cur][cur] = true;
            q.push({cur, cur, count + 1});
        }
    }
}


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int t = 1;
    while (t--)
        solve();
    return 0;
}
