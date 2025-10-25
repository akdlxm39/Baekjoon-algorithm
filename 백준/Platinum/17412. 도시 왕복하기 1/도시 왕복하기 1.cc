// https://www.acmicpc.net/problem/17412 도시 왕복하기 1
#include<bits/stdc++.h>
using namespace std;

const int MAX_NODE = 401, INF = 1e9;
const int S = 1, T = 2;

vector<int> graph[MAX_NODE];
int capacity[MAX_NODE][MAX_NODE], flow[MAX_NODE][MAX_NODE];
int previous[MAX_NODE];
int n, p;

int edmonds_karp() {
    int ret = 0;
    while (true) {
        memset(previous, -1, sizeof(previous));
        queue<int> q;
        q.push(S);
        previous[S] = 0;
        while (!q.empty()) {
            int cur = q.front();
            q.pop();
            for (int nxt: graph[cur]) {
                if (capacity[cur][nxt] - flow[cur][nxt] > 0 && previous[nxt] == -1) {
                    previous[nxt] = cur;
                    q.push(nxt);
                    if (nxt == T) break;
                }
            }
            if (previous[T] != -1) break;
        }
        if (previous[T] == -1) break;
        int min_flow = INF, route = T;
        while (route != S) {
            min_flow = min(min_flow, capacity[previous[route]][route] - flow[previous[route]][route]);
            route = previous[route];
        }
        route = T;
        while (route != S) {
            flow[previous[route]][route] += min_flow;
            flow[route][previous[route]] -= min_flow;
            route = previous[route];
        }
        ret += min_flow;
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
    cout << edmonds_karp() << '\n';
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
