#include<bits/stdc++.h>

using namespace std;
const pair<int, int> DIR[4] = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
int seat[21][21], n;
map<int, set<int> > favorite;

int get_priority(int a, int x, int y) {
    int ret = 0;
    for (auto [dx, dy]: DIR) {
        int nx = x + dx, ny = y + dy;
        if (nx < 0 || n <= nx || ny < 0 || n <= ny)
            continue;
        if (seat[nx][ny] == 0)
            ret += 1;
        else if (favorite[a].find(seat[nx][ny]) != favorite[a].end())
            ret += 5;
    }
    return ret;
}

void sit(int a) {
    int priority = -1, x, y;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (seat[i][j] != 0) continue;
            int tp = get_priority(a, i, j);
            if (tp > priority) {
                priority = tp, x = i, y = j;
            }
        }
    }
    seat[x][y] = a;
}

int get_satisfaction() {
    int ret = 0;
    for (int x = 0; x < n; x++) {
        for (int y = 0; y < n; y++) {
            int tmp = 1;
            for (auto [dx, dy]: DIR) {
                int nx = x + dx, ny = y + dy;
                if (nx < 0 || n <= nx || ny < 0 || n <= ny)
                    continue;
                if (favorite[seat[x][y]].find(seat[nx][ny]) != favorite[seat[x][y]].end())
                    tmp *= 10;
            }
            ret += tmp / 10;
        }
    }
    return ret;
}

void solve() {
    cin >> n;
    for (int i = 0, a; i < n * n; i++) {
        cin >> a;
        for (int j = 0, b; j < 4; j++) {
            cin >> b;
            favorite[a].insert(b);
        }
        sit(a);
    }
    // for (int i = 0; i < n; i++) {
    //     for (int j = 0; j < n; j++) {
    //         cout << seat[i][j] << ' ';
    //     }
    //     cout << '\n';
    // }
    cout << get_satisfaction() << '\n';
}


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int t = 1;
    while (t--)
        solve();
    return 0;
}
