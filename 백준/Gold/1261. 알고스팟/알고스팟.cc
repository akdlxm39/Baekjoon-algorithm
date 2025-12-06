// https://www.acmicpc.net/problem/1261 알고스팟
#include<bits/stdc++.h>
using namespace std;

const vector<array<int, 2> > DIR = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

int n, m, cnt[100][100];
vector<string> map_;
deque<array<int, 2> > dq;

int bfs01() {
    memset(cnt, -1, sizeof(cnt));
    dq.push_back({0, 0});
    cnt[0][0] = 0;
    while (!dq.empty()) {
        auto [x, y] = dq.front();
        dq.pop_front();
        for (auto &[dx, dy]: DIR) {
            int nx = x + dx, ny = y + dy;
            if (nx < 0 || m <= nx || ny < 0 || n <= ny || cnt[nx][ny] != -1) continue;
            if (nx == m - 1 && ny == n - 1)
                return cnt[x][y];
            if (map_[nx][ny] == '0') {
                dq.push_front({nx, ny});
                cnt[nx][ny] = cnt[x][y];
            } else {
                dq.push_back({nx, ny});
                cnt[nx][ny] = cnt[x][y] + 1;
            }
        }
    }
    return cnt[m - 1][n - 1];
}

void solve() {
    cin >> n >> m;
    map_.resize(m);
    for (string &s: map_)
        cin >> s;
    cout << bfs01() << '\n';
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int t = 1;
    while (t--) solve();
    return 0;
}
