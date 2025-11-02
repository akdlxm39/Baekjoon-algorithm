// https://www.acmicpc.net/problem/2842 집배원 한상덕
#include<bits/stdc++.h>
using namespace std;

const vector<tuple<int, int> > DIR8 = {
    {-1, -1}, {-1, 0}, {-1, 1}, {0, -1},
    {0, 1}, {1, -1}, {1, 0}, {1, 1}
};
const int MAX = 50, INF = 1000001;

int n, px, py, altitude[MAX][MAX], ans = INF, cnt_k;
string map_[MAX];
vector<int> altitudes;

bool bfs(int l, int r) {
    if (altitude[px][py] < l || r < altitude[px][py]) return false;
    int cnt = 0;
    bool visited[MAX][MAX] = {false};
    queue<array<int, 2> > q;
    q.push({px, py});
    visited[px][py] = true;
    while (!q.empty()) {
        auto [cx, cy] = q.front();
        q.pop();
        for (auto [dx, dy]: DIR8) {
            int nx = cx + dx, ny = cy + dy;
            if (nx < 0 || n <= nx || ny < 0 || n <= ny || visited[nx][ny]) continue;
            visited[nx][ny] = true;
            if (altitude[nx][ny] < l || r < altitude[nx][ny]) continue;
            if (map_[nx][ny] == 'K') ++cnt;
            q.push({nx, ny});
        }
    }
    return cnt == cnt_k;
}


void solve() {
    cin >> n;
    for (int i = 0; i < n; ++i) {
        cin >> map_[i];
        for (int j = 0; j < n; ++j) {
            if (map_[i][j] == 'P')
                px = i, py = j;
            else if (map_[i][j] == 'K')
                ++cnt_k;
        }
    }
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < n; ++j) {
            cin >> altitude[i][j];
            altitudes.push_back(altitude[i][j]);
        }
    sort(altitudes.begin(), altitudes.end());
    for (int i = 0; i < n * n; ++i) {
        int cur = altitudes[i];
        int l = i, r = n * n - 1, res = -1;
        while (l <= r) {
            int mid = (l + r) / 2;
            if (bfs(cur, altitudes[mid])) {
                res = mid;
                r = mid - 1;
            } else {
                l = mid + 1;
            }
        }
        if (res == -1) break;
        ans = min(ans, altitudes[res] - cur);
    }
    cout << ans << '\n';
}


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int t = 1;
    while (t--)
        solve();
    return 0;
}
