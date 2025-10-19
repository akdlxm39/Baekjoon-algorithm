#include<bits/stdc++.h>
using namespace std;

typedef long long ll;

const int MAX = INT_MAX;

int graph[401][401], v, e;


void solve() {
    cin >> v >> e;
    for (int i = 1; i <= v; i++)
        fill(graph[i], graph[i] + v + 1, MAX);
    for (int i = 0; i < e; i++) {
        int a, b, c;
        cin >> a >> b >> c;
        graph[a][b] = c;
    }
    for (int k = 1; k <= v; k++) {
        for (int i = 1; i <= v; i++) {
            if (i == k || graph[i][k] == MAX) continue;
            for (int j = 1; j <= v; j++) {
                if (j == k || graph[k][j] == MAX) continue;
                if (graph[i][j] > graph[i][k] + graph[k][j])
                    graph[i][j] = graph[i][k] + graph[k][j];
            }
        }
    }
    int ans = MAX;
    for (int i = 1; i <= v; i++)
        if (ans > graph[i][i])
            ans = graph[i][i];
    cout << (ans != MAX ? ans : -1) << '\n';
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
