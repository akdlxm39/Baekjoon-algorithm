#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

struct Point
{
    int y, x;
    inline Point operator+(Point other) const;
    inline void operator+=(Point other);
    inline bool isVaild() const;
    inline char &map();
};

const string TANK = "^v<>";
const Point DIR[4] = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

int height, width, n;
string map_[21], commands;
Point cur;
int curDir;

inline Point Point::operator+(Point other) const
{
    return {y + other.y, x + other.x};
}

inline void Point::operator+=(Point other)
{
    y += other.y;
    x += other.x;
}

inline bool Point::isVaild() const
{
    return 0 <= y && y < height && 0 <= x && x < width;
}

inline char &Point::map()
{
    return map_[y][x];
}

inline void move(int di)
{
    curDir = di;
    cur.map() = TANK[curDir];
    Point nxt = cur + DIR[curDir];
    if (nxt.isVaild() && nxt.map() == '.')
    {
        swap(cur.map(), nxt.map());
        cur = nxt;
    }
}

inline void shoot()
{
    Point shell = cur + DIR[curDir];
    while (shell.isVaild())
    {
        if (shell.map() == '*')
        {
            shell.map() = '.';
            break;
        }
        else if (shell.map() == '#')
        {
            break;
        }
        shell += DIR[curDir];
    }
}

void init()
{
}

void input()
{
    cin >> height >> width;
    for (int i = 0; i < height; ++i)
    {
        cin >> map_[i];
        size_t j = map_[i].find_first_of(TANK);
        if (j != string::npos)
        {
            cur.y = i, cur.x = j;
            curDir = TANK.find(map_[i][j]);
        }
    }
    cin >> n >> commands;
}

void solve()
{
    for (auto command : commands)
    {
        if (command == 'U')
            move(0);
        else if (command == 'D')
            move(1);
        else if (command == 'L')
            move(2);
        else if (command == 'R')
            move(3);
        else if (command == 'S')
            shoot();
    }
}

void output()
{
    for (int i = 0; i < height; ++i)
        cout << map_[i] << '\n';
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    for (int test_case = 1; test_case <= T; ++test_case)
    {
        init();
        input();
        solve();
        cout << '#' << test_case << ' ';
        output();
    }
}