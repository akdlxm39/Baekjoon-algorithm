#include <bits/stdc++.h>
#include <unordered_map>
using namespace std;

const int INF = 987654321;

struct pos {
    int x, y;
};

const vector<pos> DIR = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

const vector<vector<pos> > TUNNELS = {
    {},
    {{1, 0}, {-1, 0}, {0, 1}, {0, -1}},
    {{1, 0}, {-1, 0}},
    {{0, 1}, {0, -1}},
    {{-1, 0}, {0, 1}},
    {{0, 1}, {1, 0}},
    {{1, 0}, {0, -1}},
    {{0, -1}, {-1, 0}}
};
int n, m, r, c, l, board[51][51];
bool visited[51][51];


bool is_connected(int dx, int dy, int nxt) {
    if (nxt == 0) return 0;
    for (const pos &nxt_d: TUNNELS[nxt]) {
        if (dx + nxt_d.x == 0 && dy + nxt_d.y == 0) {
            return true;
        }
    }
    return false;
}

int bfs() {
    int res = 1;
    fill_n(&visited[0][0], 51 * 51, false);
    visited[r][c] = true;
    queue<pos> q;
    q.push({r, c});
    while (--l) {
        queue<pos> nxt_q;
        while (!q.empty()) {
            int x = q.front().x, y = q.front().y;
            q.pop();
            for (const pos &d: TUNNELS[board[x][y]]) {
                int nx = x + d.x, ny = y + d.y;
                if (nx < 0 || n <= nx || ny < 0 || m <= ny || visited[nx][ny]) continue;
                if (is_connected(d.x, d.y, board[nx][ny])) {
                    visited[nx][ny] = true;
                    nxt_q.push({nx, ny});
                    ++res;
                }
            }
        }
        q = nxt_q;
    }
    return res;
}


void solve() {
    cin >> n >> m >> r >> c >> l;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            cin >> board[i][j];
        }
    }

    cout << bfs() << '\n';
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int T = 1;
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        cout << '#' << t << ' ';
        solve();
    }
}
