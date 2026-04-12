#include <iostream>
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
    int mask() const;
};
constexpr Point DIR[5] = {{0, 0}, {-1, 0}, {0, 1}, {1, 0}, {0, -1}};

int m, a, ans;
int moves[2][101];
int map_[11][11];
int power[8];
Point user[2];

inline int Point::mask() const
{
    return map_[y][x];
}

void setBC(Point bc, int c, int mask)
{
    for (int i = 1; i <= 10; ++i)
        for (int j = 1; j <= 10; ++j)
            if (abs(i - bc.y) + abs(j - bc.x) <= c)
                map_[i][j] |= mask;
}

int maxCharge(int maskA, int maskB)
{
    int ret = 0;
    for (int i1 = 0; i1 < a; ++i1)
    {
        int p1 = (maskA & (1 << i1)) ? power[i1] : 0;
        for (int i2 = 0; i2 < a; ++i2)
        {
            int p2 = (maskB & (1 << i2)) ? power[i2] : 0;
            if (i1 == i2 && p1 && p2)
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
    user[0] = {1, 1};
    user[1] = {10, 10};
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
        setBC({y, x}, c, 1 << i);
    }
}

void solve()
{
    for (int j = 0; j <= m; ++j)
    {
        for (int i = 0; i < 2; ++i)
            user[i] += DIR[moves[i][j]];
        ans += maxCharge(user[0].mask(), user[1].mask());
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