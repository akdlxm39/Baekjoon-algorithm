// https://www.acmicpc.net/problem/2316 도시 왕복하기 2
#include<bits/stdc++.h>
using namespace std;

const int MAX_NODE = 801, INF = 1e9;

vector<int> graph[MAX_NODE];
int capacity[MAX_NODE][MAX_NODE], flow[MAX_NODE][MAX_NODE];
bool visited[MAX_NODE];
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


int dinic(int s, int t) {
    int ret = 0;
    while (bfs(s, t)) {
        fill(work, work + MAX_NODE, 0);
        while (int cur_flow = dfs(s, t, INF))
            ret += cur_flow;
    }
    return ret;
}

void solve() {
    cin >> n >> p;
    for (int i = 1; i <= n; ++i) {
        graph[i * 2 - 1].push_back(i * 2);
        graph[i * 2].push_back(i * 2 - 1);
        capacity[i * 2 - 1][i * 2] = 1;
    }
    for (int i = 0, a, b; i < p; ++i) {
        cin >> a >> b;
        graph[a * 2].push_back(b * 2 - 1);
        graph[b * 2 - 1].push_back(a * 2);
        capacity[a * 2][b * 2 - 1] = 1;
        graph[a * 2 - 1].push_back(b * 2);
        graph[b * 2].push_back(a * 2 - 1);
        capacity[b * 2][a * 2 - 1] = 1;
    }
    cout << dinic(2, 3) << '\n';
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int t = 1;
    while (t--)
        solve();
    return 0;
}
