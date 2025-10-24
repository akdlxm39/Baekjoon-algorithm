// https://www.acmicpc.net/problem/6086 최대 유량
#include<bits/stdc++.h>
using namespace std;

const int MAXNODE = 52;
const int INF = 1e9;

int ctoi(char c) { return c < 'a' ? c - 'A' : c - 'a' + 26; }

vector<int> graph[MAXNODE];
int capacity[MAXNODE][MAXNODE], flow[MAXNODE][MAXNODE];
int previous[MAXNODE];
int n;
const int S = ctoi('A'), T = ctoi('Z');

int edmonds_karp() {
    int ret = 0;
    while (true) {
        queue<int> q({S});
        memset(previous, -1, sizeof(previous));
        while (!q.empty()) {
            int cur = q.front();
            q.pop();
            for (int nxt: graph[cur]) {
                if (capacity[cur][nxt] - flow[cur][nxt] > 0 && previous[nxt] == -1) {
                    previous[nxt] = cur;
                    q.push(nxt);
                    if (nxt == T)
                        break;
                }
            }
            if (previous[T] != -1)
                break;
        }
        if (previous[T] == -1)
            break;
        int f = INF, p = T;
        while (p != S) {
            f = min(f, capacity[previous[p]][p] - flow[previous[p]][p]);
            p = previous[p];
        }
        p = T;
        while (p != S) {
            flow[previous[p]][p] += f;
            flow[p][previous[p]] -= f;
            p = previous[p];
        }
        ret += f;
    }
    return ret;
}

void solve() {
    cin >> n;
    for (int i = 0; i < n; ++i) {
        int u, v, c;
        char a, b;
        cin >> a >> b >> c;
        u = ctoi(a), v = ctoi(b);
        graph[u].push_back(v);
        graph[v].push_back(u);
        capacity[u][v] += c;
        capacity[v][u] += c;
    }
    cout << edmonds_karp() << endl;
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
