// https://www.acmicpc.net/problem/2188 축사 배정
#include<bits/stdc++.h>
using namespace std;

const int MAX_NODE = 402, INF = 1e9;

vector<int> graph[MAX_NODE];
int capacity[MAX_NODE][MAX_NODE], flow[MAX_NODE][MAX_NODE];
int previous[MAX_NODE];
int n, m;

int edmonds_karp(int s, int t) {
    int ret = 0;
    while (true) {
        fill(previous, previous + MAX_NODE, -1);
        queue<int> q;
        q.push(s);
        previous[s] = 0;
        while (!q.empty()) {
            int cur = q.front();
            q.pop();
            for (int nxt: graph[cur]) {
                if (previous[nxt] == -1 && capacity[cur][nxt] - flow[cur][nxt] > 0) {
                    previous[nxt] = cur;
                    q.push(nxt);
                }
            }
        }
        if (previous[t] == -1) break;
        int min_flow = INF;
        for (int i = t; i != s; i = previous[i])
            min_flow = min(min_flow, capacity[previous[i]][i] - flow[previous[i]][i]);
        for (int i = t; i != s; i = previous[i]) {
            flow[previous[i]][i] += min_flow;
            flow[i][previous[i]] -= min_flow;
        }
        ret += min_flow;
    }
    return ret;
}

void solve() {
    cin >> n >> m;
    int s = 0, t = n + m + 1;
    for (int i = 1, k, x; i <= n; ++i) {
        cin >> k;
        while (k--) {
            cin >> x;
            x += n;
            graph[i].push_back(x);
            graph[x].push_back(i);
            capacity[i][x] = 1;
        }
        graph[s].push_back(i);
        capacity[s][i] = 1;
    }
    for (int i = n + 1; i <= n + m; ++i) {
        graph[i].push_back(t);
        capacity[i][t] = 1;
    }
    cout << edmonds_karp(s, t) << '\n';
}


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int t = 1;
    while (t--)
        solve();
    return 0;
}
