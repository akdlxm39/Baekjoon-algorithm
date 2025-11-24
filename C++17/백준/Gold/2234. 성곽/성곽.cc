// https://www.acmicpc.net/problem/2234 성곽
#include<bits/stdc++.h>
using namespace std;

const vector<array<int, 2> > DIR = {
    {0, -1}, {-1, 0}, {0, 1}, {1, 0}
};

int n, m, id, max_size;

vector<int> room_size;
vector<vector<int> > wall, room;
vector<vector<bool> > visited;

void bfs1(int x, int y) {
    queue<array<int, 2> > q;
    q.push({x, y});
    visited[x][y] = true;
    int cnt = 0;
    while (!q.empty()) {
        auto [cx, cy] = q.front();
        q.pop();
        room[cx][cy] = id;
        ++cnt;
        for (int i = 0; i < 4; ++i) {
            auto &[dx, dy] = DIR[i];
            int nx = cx + dx, ny = cy + dy;
            if (wall[cx][cy] & 1 << i || visited[nx][ny]) continue;
            visited[nx][ny] = true;
            q.push({nx, ny});
        }
    }
    room_size.push_back(cnt);
    max_size = max(max_size, cnt);
    id++;
}

int bfs2() {
    int ret = 0;
    vector check(room_size.size(), 0);
    deque<array<int, 3> > dq;
    dq.push_back({0, 0, 0});
    visited = vector(m, vector(n, false));
    visited[0][0] = true;
    while (!dq.empty()) {
        auto [id, cx, cy] = dq.front();
        dq.pop_front();
        ++check[id];
        for (auto &[dx, dy]: DIR) {
            int nx = cx + dx, ny = cy + dy;
            if (nx < 0 || m <= nx || ny < 0 || n <= ny) continue;
            int nid = room[nx][ny];
            if (nid == id) {
                if (visited[nx][ny]) continue;
                visited[nx][ny] = true;
                dq.push_front({id, nx, ny});
            } else {
                if (check[nid] < room_size[nid])
                    ret = max(ret, room_size[nid] + room_size[id]);
                if (visited[nx][ny]) continue;
                visited[nx][ny] = true;
                dq.push_back({nid, nx, ny});
            }
        }
    }

    return ret;
}

void solve() {
    cin >> n >> m;
    wall = vector(m, vector(n, 0));
    room = vector(m, vector(n, 0));
    visited = vector(m, vector(n, false));
    for (auto &line: wall)
        for (auto &w: line)
            cin >> w;
    for (int i = 0; i < m; ++i)
        for (int j = 0; j < n; ++j)
            if (!visited[i][j])
                bfs1(i, j);
    cout << id << '\n';
    cout << max_size << '\n';
    cout << bfs2() << '\n';
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int t = 1;
    while (t--) solve();
    return 0;
}
