#include <iostream>
#include <queue>
#include <cstring>

using namespace std;

struct Point
{
    int y, x;
    void operator+=(Point other)
    {
        y += other.y;
        x += other.x;
    }
};
constexpr Point DIR[5] = {{0, 0}, {-1, 0}, {0, 1}, {1, 0}, {0, -1}};

int m, a, ans;
int moves[2][101];
int map_[11][11];
int power[8];

void bfsBC(int y, int x, int c, int mask)
{
    for (int i = 1; i <= 10; ++i)
        for (int j = 1; j <= 10; ++j)
            if (abs(i - y) + abs(j - x) <= c)
                map_[i][j] |= mask;
}

int maxCharge(int bc1, int bc2)
{
    int ret = 0;
    for (int i = 0; i < a; ++i)
    {
        int p1 = (bc1 & (1 << i)) ? power[i] : 0;
        for (int j = 0; j < a; ++j)
        {
            int p2 = (bc2 & (1 << j)) ? power[j] : 0;
            if (i == j && p1 && p2)
                ret = max(ret, p1);
            else
                ret = max(ret, p1 + p2);
        }
    }
    return ret;
}

void init()
{
    memset(map_, 0, sizeof(map_));
    ans = 0;
}

void input()
{
    cin >> m >> a;
    for (int i = 0; i < 2; ++i)
        for (int j = 1; j <= m; ++j)
            cin >> moves[i][j];
    for (int i = 0; i < a; ++i)
    {
        int y, x, c;
        cin >> x >> y >> c >> power[i];
        bfsBC(y, x, c, 1 << i);
    }
}

void solve()
{

    Point user[2] = {{1, 1}, {10, 10}};
    for (int j = 0; j <= m; ++j)
    {
        for (int i = 0; i < 2; ++i)
            user[i] += DIR[moves[i][j]];
        ans += maxCharge(map_[user[0].y][user[0].x], map_[user[1].y][user[1].x]);
    }
}

void output(int testCase)
{
    cout << '#' << testCase << ' ' << ans << '\n';
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    for (int testCase = 1; testCase <= T; ++testCase)
    {
        init();
        input();
        solve();
        output(testCase);
    }

    return 0;
}