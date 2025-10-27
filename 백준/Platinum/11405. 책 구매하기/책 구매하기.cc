// https://www.acmicpc.net/problem/11405 책 구매하기
#include<bits/stdc++.h>
using namespace std;

const int MAX_NODE = 202, INF = 1e9;

vector<int> graph[MAX_NODE];
int cost[MAX_NODE][MAX_NODE], dist[MAX_NODE], previous[MAX_NODE];
bool in_queue[MAX_NODE];
int capacity[MAX_NODE][MAX_NODE], flow[MAX_NODE][MAX_NODE];
int n, m;

int spfa_edmonds_karp(int s, int t) {
    int ret = 0;
    while (true) {
        fill(dist, dist + MAX_NODE, INF);
        fill(previous, previous + MAX_NODE, -1);
        fill(in_queue, in_queue + MAX_NODE, false);
        queue<int> q;
        q.push(s);
        in_queue[s] = true;
        dist[s] = 0;
        while (!q.empty()) {
            int cur = q.front();
            q.pop();
            in_queue[cur] = false;
            for (int nxt: graph[cur]) {
                if (capacity[cur][nxt] - flow[cur][nxt] > 0 && dist[cur] + cost[cur][nxt] < dist[nxt]) {
                    dist[nxt] = dist[cur] + cost[cur][nxt];
                    previous[nxt] = cur;
                    if (!in_queue[nxt]) {
                        q.push(nxt);
                        in_queue[nxt] = true;
                    }
                }
            }
        }
        if (previous[t] == -1) break;
        int min_flow = INF;
        for (int route = t; route != s; route = previous[route])
            min_flow = min(min_flow, capacity[previous[route]][route] - flow[previous[route]][route]);
        for (int route = t; route != s; route = previous[route]) {
            flow[previous[route]][route] += min_flow;
            flow[route][previous[route]] -= min_flow;
            ret += min_flow * cost[previous[route]][route];
        }
    }
    return ret;
}


void solve() {
    cin >> n >> m;
    int s = 0, t = n + m + 1;
    for (int j = m + 1; j <= m + n; ++j) {
        cin >> capacity[j][t];
        graph[j].push_back(t);
        graph[t].push_back(j);
    }
    for (int i = 1; i <= m; ++i) {
        cin >> capacity[s][i];
        graph[s].push_back(i);
        graph[i].push_back(s);
    }
    for (int i = 1; i <= m; ++i)
        for (int j = m + 1; j <= m + n; ++j) {
            cin >> cost[i][j];
            cost[j][i] = -cost[i][j];
            capacity[i][j] = INF;
            graph[i].push_back(j);
            graph[j].push_back(i);
        }
    cout << spfa_edmonds_karp(s, t) << '\n';
}


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int t = 1;
    while (t--)
        solve();
    return 0;
}
