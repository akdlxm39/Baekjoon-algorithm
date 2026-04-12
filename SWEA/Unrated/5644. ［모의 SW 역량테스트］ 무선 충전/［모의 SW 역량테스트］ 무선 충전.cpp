#include <iostream>
#include <queue>
#include <cstring>

using namespace std;

struct Point
{
    int y, x;
    Point operator+(Point other) const
    {
        return {y + other.y, x + other.x};
    }
    void operator+=(Point other)
    {
        y += other.y;
        x += other.x;
    }
    bool isValid() const
    {
        return 1 <= y && y <= 10 && 1 <= x && x <= 10;
    }
};
constexpr Point DIR[5] = {{0, 0}, {-1, 0}, {0, 1}, {1, 0}, {0, -1}};

int m, a, ans;
int moves[2][101];
int map_[11][11];
int power[8];

void bfsBC(int y, int x, int c, int mask)
{
    queue<Point> q, nxt_q;
    q.push({y, x});
    map_[y][x] |= mask;
    while (c--)
    {
        while (!q.empty())
        {
            Point cur = q.front();
            q.pop();
            for (Point d : DIR)
            {
                Point nxt = cur + d;
                if (!nxt.isValid() || map_[nxt.y][nxt.x] & mask)
                    continue;
                nxt_q.push(nxt);
                map_[nxt.y][nxt.x] |= mask;
            }
        }
        q.swap(nxt_q);
    }
}

int maxCharge(int bc1, int bc2)
{
    int ret = 0;
    if (bc1 && bc2)
    {
        for (int i = 0; i < a; ++i)
        {
            if (!(bc1 & (1 << i)))
                continue;
            for (int j = 0; j < a; ++j)
            {
                if (!(bc2 & (1 << j)))
                    continue;
                if (i == j)
                    ret = max(ret, power[i]);
                else
                    ret = max(ret, power[i] + power[j]);
            }
        }
    }
    else if (bc1)
    {
        for (int i = 0; i < a; ++i)
            if (bc1 & (1 << i))
                ret = max(ret, power[i]);
    }
    else if (bc2)
    {
        for (int i = 0; i < a; ++i)
            if (bc2 & (1 << i))
                ret = max(ret, power[i]);
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