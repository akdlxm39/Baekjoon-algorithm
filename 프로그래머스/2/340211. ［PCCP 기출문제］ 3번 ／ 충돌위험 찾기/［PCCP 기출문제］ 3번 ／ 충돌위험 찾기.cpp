#include <set>
#include <string>
#include <vector>

using namespace std;

struct Robot
{
    int r, c;
    int nxt;
    void move(const vector<vector<int>> &points, const vector<int> &route)
    {
        if (nxt == -1 || nxt == route.size())
        {
            nxt = r = c = -1;
            return;
        }
        int to = route[nxt] - 1;
        if (r < points[to][0])
            r++;
        else if (r > points[to][0])
            r--;
        else if (c < points[to][1])
            c++;
        else if (c > points[to][1])
            c--;
        if (r == points[to][0] && c == points[to][1])
            nxt++;
    }
    bool operator==(const Robot &other) const
    {
        return other.nxt != -1 && r == other.r && c == other.c;
    }
};

int solution(vector<vector<int>> points, vector<vector<int>> routes)
{
    int answer = 0;
    int cnt = routes.size();
    vector<Robot> robots;
    set<int> dangerPoint;
    for (const auto &route : routes)
    {
        Robot robot = {points[route[0] - 1][0], points[route[0] - 1][1], 1};
        for (const auto &other : robots)
            if (robot == other)
                dangerPoint.insert(robot.r * 1000 + robot.c);
        robots.push_back(robot);
    }
    answer += dangerPoint.size();
    for (int fin = 0; fin < cnt;)
    {
        dangerPoint.clear();
        for (int i = 0; i < cnt; ++i)
        {
            if (robots[i].nxt == -1)
                continue;
            robots[i].move(points, routes[i]);
            if (robots[i].nxt == routes[i].size())
                fin++;
            for (int j = 0; j < i; ++j)
                if (robots[i] == robots[j])
                    dangerPoint.insert(robots[i].r * 1000 + robots[i].c);
        }
        answer += dangerPoint.size();
    }
    return answer;
}