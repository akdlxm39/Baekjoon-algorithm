// https://www.acmicpc.net/problem/17412 도시 왕복하기 1
#include<bits/stdc++.h>
using namespace std;

const int MAX_NODE = 401, INF = 1e9;
const int S = 1, T = 2;

vector<int> graph[MAX_NODE];
int capacity[MAX_NODE][MAX_NODE], flow[MAX_NODE][MAX_NODE];
int level_graph[MAX_NODE], work[MAX_NODE];
int n, p;

bool bfs(int s, int t) {
    fill(level_graph, level_graph + MAX_NODE, -1);
    queue<int> q;
    q.push(s);
    level_graph[s] = 0;
    while (!q.empty()) {
        int cur = q.front();
        q.pop();
        for (int nxt: graph[cur]) {
            if (level_graph[nxt] == -1 && capacity[cur][nxt] - flow[cur][nxt] > 0) {
                level_graph[nxt] = level_graph[cur] + 1;
                q.push(nxt);
            }
        }
    }
    return level_graph[t] != -1;
}

int dfs(int cur, int t, int min_flow) {
    if (cur == t) return min_flow;
    for (int &i = work[cur]; i < graph[cur].size(); ++i) {
        int nxt = graph[cur][i];
        if (level_graph[nxt] == level_graph[cur] + 1 && capacity[cur][nxt] - flow[cur][nxt] > 0) {
            int cur_flow = dfs(nxt, t, min(min_flow, capacity[cur][nxt] - flow[cur][nxt]));
            if (cur_flow > 0) {
                flow[cur][nxt] += cur_flow;
                flow[nxt][cur] -= cur_flow;
                return cur_flow;
            }
        }
    }
    return 0;
}

int dinic() {
    int ret = 0;
    while (bfs(S, T)) {
        fill(work, work + MAX_NODE, 0);
        while (int cur_flow = dfs(S, T, INF))
            ret += cur_flow;
    }
    return ret;
}

void solve() {
    cin >> n >> p;
    for (int i = 0, u, v; i < p; ++i) {
        cin >> u >> v;
        graph[u].push_back(v);
        graph[v].push_back(u);
        capacity[u][v] += 1;
    }
    cout << dinic() << '\n';
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int T = 1;
    for (int t = 0; t < T; t++) {
        solve();
    }
    return 0;
}
