#include <algorithm>
#include <string>
#include <vector>

using namespace std;

int solution(vector<vector<int>> targets)
{
    int answer = 0;
    for (auto &target : targets)
    {
        target[0] = target[0] * 2 + 1;
        target[1] = target[1] * 2 - 1;
    }
    sort(targets.begin(), targets.end(),
         [](const vector<int> &a, const vector<int> &b) { return a[1] != b[1] ? a[1] < b[1] : a[0] < b[0]; });
    int cur = 0;
    for (const auto &target : targets)
    {
        if (cur < target[0])
        {
            cur = target[1];
            answer++;
        }
    }
    return answer;
}