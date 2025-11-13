// https://www.acmicpc.net/problem/2665 미로만들기
#include<bits/stdc++.h>
using namespace std;

const int INF = 100'001;
const vector<array<int, 2> > DIR = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};

vector<string> maze;
int n;

int bfs() {
    vector<vector<bool> > visited(n, vector<bool>(n, false));
    deque<array<int, 3> > dq;
    dq.push_front({0, 0, 0});
    visited[0][0] = 0;
    while (!dq.empty()) {
        auto [cx, cy, cnt] = dq.front();
        dq.pop_front();
        for (auto [dx, dy]: DIR) {
            int nx = cx + dx, ny = cy + dy;
            if (nx < 0 || n <= nx || ny < 0 || n <= ny || visited[nx][ny]) continue;
            if (nx == n - 1 && ny == n - 1) return cnt;
            visited[nx][ny] = true;
            if (maze[nx][ny] == '1') {
                dq.push_front({nx, ny, cnt});
            } else {
                dq.push_back({nx, ny, cnt + 1});
            }
        }
    }
    return -1;
}

void solve() {
    cin >> n;
    maze.resize(n);
    for (string &s: maze)
        cin >> s;
    cout << bfs() << '\n';
}


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int t = 1;
    while (t--) solve();
    return 0;
}
