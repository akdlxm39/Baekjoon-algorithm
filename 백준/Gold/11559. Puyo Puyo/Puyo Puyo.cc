#include<bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;

#define FAST_IO ios_base::sync_with_stdio(0);cin.tie(NULL);
const vector<pair<int, int> > dir = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};

vector<string> board(12);
bool visited[12][6];

void print_() {
    cout << "------------------" << endl;
    for (auto x: board) {
        cout << x << endl;
    }
    cout << "------------------" << endl;
}

vector<pii> find() {
    vector<pii> res;
    memset(visited, false, sizeof(visited));
    for (int i = 0; i < 12; i++) {
        for (int j = 0; j < 6; j++) {
            if (board[i][j] == '.' || visited[i][j])
                continue;
            char cur = board[i][j];
            queue<pii> q;
            vector<pii> tmp;
            q.push({i, j});
            while (!q.empty()) {
                int x = q.front().first;
                int y = q.front().second;
                q.pop();
                for (int d = 0; d < 4; d++) {
                    int nx = x + dir[d].first;
                    int ny = y + dir[d].second;
                    if (nx < 0 || nx >= 12 || ny < 0 || ny >= 6)
                        continue;
                    if (visited[nx][ny])
                        continue;
                    if (board[nx][ny] == cur) {
                        visited[nx][ny] = true;
                        q.push({nx, ny});
                        tmp.push_back({nx, ny});
                    }
                }
            }
            if (tmp.size() >= 4) {
                for (auto pos: tmp) {
                    res.push_back(pos);
                }
            }
        }
    }
    return res;
}

void bomb(vector<pii> puyo) {
    for (auto pos: puyo) {
        board[pos.first][pos.second] = '.';
    }
    for (int j = 0; j < 6; j++) {
        queue<char> line;
        for (int i = 0; i < 12; i++) {
            if (board[i][j] != '.') {
                line.push(board[i][j]);
                board[i][j] = '.';
            }
        }
        int i = 12 - line.size();
        while (!line.empty()) {
            board[i++][j] = line.front();
            line.pop();
        }
    }
}

void solve() {
    for (int i = 0; i < 12; i++) {
        cin >> board[i];
    }
    int ans = 0;
    while (true) {
        vector<pii> puyo = find();
        if (puyo.empty())
            break;
        bomb(puyo);
        ans++;
    }
    cout << ans << endl;
}

int main() {
    FAST_IO
    int T = 1;
    for (int i = 0; i < T; i++) {
        solve();
    }
    return 0;
}
