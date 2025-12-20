// https://www.acmicpc.net/problem/2638 치즈
#include<bits/stdc++.h>
using namespace std;

const vector<array<int, 2> > DIR = {
    {0, 1}, {1, 0}, {0, -1}, {-1, 0}
};

int n, m, cheese[101][101], air[101][101];
bool visited[101][101];

int bfs01(int cnt) {
    deque<array<int, 3> > dq;
    dq.push_back({0, 0, 0});
    visited[0][0] = true;
    while (!dq.empty()) {
        auto [cx, cy, ct] = dq.front();
        dq.pop_front();
        for (const auto &[dx, dy]: DIR) {
            int nx = cx + dx, ny = cy + dy;
            if (nx < 0 || n <= nx || ny < 0 || m <= ny || visited[nx][ny]) continue;
            if (cheese[nx][ny] == 0) {
                visited[nx][ny] = true;
                dq.push_front({nx, ny, ct});
            } else if (cheese[nx][ny] == 1) {
                if (++air[nx][ny] == 2) {
                    if (--cnt == 0)
                        return ct + 1;
                    visited[nx][ny] = true;
                    dq.push_back({nx, ny, ct + 1});
                }
            }
        }
    }
    return -1;
}


void solve() {
    cin >> n >> m;
    int cnt = 0;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            cin >> cheese[i][j];
            if (cheese[i][j] == 1) ++cnt;
        }
    }
    cout << bfs01(cnt) << '\n';
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int t = 1;
    while (t--) solve();
    return 0;
}
