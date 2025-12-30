// https://www.acmicpc.net/problem/17143 낚시왕
#include<bits/stdc++.h>
using namespace std;

struct Shark {
    int x, y;
    int speed;
    int dir;
    int size;
};

int r, c, m, sharks_idx;
vector<vector<int> > water;
unordered_map<int, Shark> sharks;

int catch_shark(int j) {
    for (int i = 1; i <= r; ++i) {
        if (water[i][j]) {
            int ret = sharks[water[i][j]].size;
            sharks.erase(water[i][j]);
            return ret;
        }
    }
    return 0;
}

void move(Shark &shark) {
    int dist = shark.speed;
    while (dist) {
        if (shark.dir == 1)
            if (shark.x - dist < 1)
                dist -= shark.x - 1, shark.x = 1, shark.dir = 2;
            else
                shark.x -= dist, dist = 0;
        else if (shark.dir == 2)
            if (shark.x + dist > r)
                dist -= r - shark.x, shark.x = r, shark.dir = 1;
            else
                shark.x += dist, dist = 0;
        else if (shark.dir == 3)
            if (shark.y + dist > c)
                dist -= c - shark.y, shark.y = c, shark.dir = 4;
            else
                shark.y += dist, dist = 0;
        else if (shark.dir == 4)
            if (shark.y - dist < 1)
                dist -= shark.y - 1, shark.y = 1, shark.dir = 3;
            else
                shark.y -= dist, dist = 0;
        else;
    }
}

void move_sharks() {
    vector<vector<int> > new_water(r + 1, vector<int>(c + 1, 0));
    vector<int> del_sharks;
    for (auto &[idx, shark]: sharks) {
        move(shark);
        int &cell = new_water[shark.x][shark.y];
        if (cell == 0) {
            cell = idx;
        } else {
            Shark &other = sharks[cell];
            if (other.size < shark.size) {
                del_sharks.push_back(cell);
                cell = idx;
            } else {
                del_sharks.push_back(idx);
            }
        }
    }
    for (int idx:del_sharks)
        sharks.erase(idx);
    water = new_water;
}

void solve() {
    cin >> r >> c >> m;
    water.resize(r + 1, vector<int>(c + 1, 0));
    for (int idx = 1; idx <= m; ++idx) {
        auto &[x, y, speed, dir, size] = sharks[idx];
        cin >> x >> y >> speed >> dir >> size;
        water[x][y] = idx;
        if (dir <= 2 && r > 1)
            speed %= (r - 1) * 2;
        else if (c > 1) {
            speed %= (c - 1) * 2;
        }
    }
    int ans = 0;
    for (int j = 1; j <= c; ++j) {
        ans += catch_shark(j);
        move_sharks();
    }
    cout << ans << '\n';
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int t = 1;
    while (t--) solve();
    return 0;
}
