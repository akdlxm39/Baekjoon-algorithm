// https://www.acmicpc.net/problem/1939 중량제한
#include<bits/stdc++.h>
using namespace std;

const int MAX = 10001, INF = 1000000007;

vector<pair<int, int> > graph[MAX];
int max_weight[MAX];
bool in_queue[MAX];
int n, m;

int spfa(int s, int t) {
    queue<int> q;
    q.push(s);
    in_queue[s] = true;
    max_weight[s] = INF;
    while (!q.empty()) {
        int cur = q.front();
        q.pop();
        in_queue[cur] = false;
        for (auto [nxt, cap]: graph[cur]) {
            if (max_weight[nxt] < min(max_weight[cur], cap)) {
                max_weight[nxt] = min(max_weight[cur], cap);
                if (!in_queue[nxt]) {
                    q.push(nxt);
                    in_queue[nxt] = true;
                }
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
    cout << spfa(s, t) << '\n';
}


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int t = 1;
    while (t--) solve();
    return 0;
}
