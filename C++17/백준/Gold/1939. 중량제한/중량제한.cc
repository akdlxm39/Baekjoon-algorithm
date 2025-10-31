// https://www.acmicpc.net/problem/1939 중량제한
#include<bits/stdc++.h>
using namespace std;

const int MAX = 10001, INF = 1000000000;

vector<pair<int, int> > graph[MAX];
int max_weight[MAX];
int n, m;

int dijkstra(int s, int t) {
    priority_queue<pair<int, int> > pq;
    pq.emplace(INF, s);
    max_weight[s] = INF;
    while (!pq.empty()) {
        auto [cur_w, cur] = pq.top();
        pq.pop();
        if (cur_w < max_weight[cur]) continue;
        for (auto [nxt, cap]: graph[cur]) {
            int nxt_w = min(cur_w, cap);
            if (max_weight[nxt] < nxt_w) {
                max_weight[nxt] = nxt_w;
                pq.emplace(nxt_w, nxt);
            }
        }
    }
    return max_weight[t];
}

void solve() {
    cin >> n >> m;
    for (int i = 0, u, v, w; i < m; ++i) {
        cin >> u >> v >> w;
        graph[u].emplace_back(v, w);
        graph[v].emplace_back(u, w);
    }
    int s, t;
    cin >> s >> t;
    cout << dijkstra(s, t) << '\n';
}


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int t = 1;
    while (t--) solve();
    return 0;
}
