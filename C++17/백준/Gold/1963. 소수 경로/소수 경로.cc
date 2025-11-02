// https://www.acmicpc.net/problem/1963 소수 경로
#include<bits/stdc++.h>
using namespace std;

const int MAX = 10000;

bool is_prime[MAX], visited[MAX];
vector<int> graph[MAX];

void make_prime() {
    fill(is_prime, is_prime + MAX, true);
    is_prime[0] = is_prime[1] = false;
    for (int i = 2; i * i <= MAX; ++i)
        if (is_prime[i])
            for (int j = i + i; j < MAX; j += i)
                is_prime[j] = false;
}

void make_graph() {
    make_prime();
    fill(visited, visited + MAX, false);
    for (int i = 1000; i < 10000; ++i) {
        if (!is_prime[i] || visited[i]) continue;
        visited[i] = true;
        queue<int> q;
        q.push(i);
        while (!q.empty()) {
            int cur = q.front();
            q.pop();
            for (int x = 1, y = 10; x <= 1000; x *= 10, y *= 10) {
                for (int nxt = (cur / y) * y + cur % x;
                     nxt < (cur / y + 1) * y; nxt += x) {
                    if (nxt >= 1000 && is_prime[nxt]) {
                        graph[cur].push_back(nxt);
                        graph[nxt].push_back(cur);
                        if (!visited[nxt]) {
                            visited[nxt] = true;
                            q.push(nxt);
                        }
                    }
                }
            }
        }
    }
}

int n, m;

int bfs(int s, int t) {
    if (s == t) return 0;
    fill(visited, visited + MAX, false);
    queue<tuple<int, int> > q;
    q.emplace(s, 1);
    visited[s] = true;
    while (!q.empty()) {
        auto [cur, cnt] = q.front();
        q.pop();
        for (int nxt: graph[cur]) {
            if (visited[nxt]) continue;
            if (nxt == t) return cnt;
            visited[nxt] = true;
            q.emplace(nxt, cnt + 1);
        }
    }
    return -1;
}

void solve() {
    cin >> n >> m;
    int ans = bfs(n, m);
    if (ans == -1)
        cout << "Impossible\n";
    else
        cout << ans << '\n';
}


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    make_graph();
    int t = 1;
    cin >> t;
    while (t--)
        solve();
    return 0;
}
