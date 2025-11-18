// https://www.acmicpc.net/problem/1941 소문난 칠공주
#include<bits/stdc++.h>
using namespace std;

constexpr int DIR[4] = {-1, 1, -7, 7};

string seats;
int dict[25];
bool ismember[49], visited[49];

bool bfs(int s) {
    queue<int> q;
    q.push(s);
    fill(visited, visited + 49, false);
    int total = 0, s_cnt = 0;
    while (!q.empty()) {
        int cur = q.front();
        q.pop();
        for (auto &d: DIR) {
            int nxt = cur + d;
            if (ismember[nxt] && !visited[nxt]) {
                q.push(nxt);
                visited[nxt] = true;
                ++total;
                s_cnt += seats[nxt] == 'S';
            }
        }
    }
    return total == 7 && s_cnt >= 4;
}

int bruteforce(int depth, int nxt) {
    if (depth == 7) {
        return bfs(dict[nxt - 1]);
    }
    int ret = 0;
    for (int i = nxt; i < 25; ++i) {
        ismember[dict[i]] = true;
        ret += bruteforce(depth + 1, i + 1);
        ismember[dict[i]] = false;
    }
    return ret;
}

void solve() {
    fill(dict, dict + 25, -1);
    seats += "XXXXXXX";
    for (int i = 0; i < 5; ++i) {
        string s;
        cin >> s;
        seats += "X" + s + "X";
        for (int j = 0; j < 5; ++j) {
            dict[i * 5 + j] = 8 + 7 * i + j;
        }
    }
    seats += "XXXXXXX";
    // cout << seats << '\n';
    // for (auto d: dict)  cout << d << ' ';
    cout << bruteforce(0, 0) << '\n';
}


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int t = 1;
    while (t--) solve();
    return 0;
}
