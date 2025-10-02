#include<bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;

#define FAST_IO ios_base::sync_with_stdio(0);cin.tie(NULL);

const int MAX = 501;

int adj[MAX][MAX], n, m, ans;

void show() {
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            if (adj[i][j] == MAX)
                cout << "M ";
            else
                cout << adj[i][j] << " ";
        }
        cout << endl;
    }
}

void solve() {
    cin >> n >> m;
    for (int i = 1; i <= n; i++) {
        fill(adj[i], adj[i] + n + 1, MAX);
        adj[i][i] = 0;
    }
    for (int i = 0; i < m; i++) {
        int a, b;
        cin >> a >> b;
        adj[a][b] = 1;
        adj[b][a] = -1;
    }
    for (int k = 1; k <= n; k++) {
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                if (adj[i][k] == MAX || adj[k][j] == MAX) continue;
                if (adj[i][k] < 0 && adj[k][j] < 0) {
                    if (adj[i][j] == MAX) adj[i][j] = -MAX;
                    adj[i][j] = max(adj[i][j], adj[i][k] + adj[k][j]);
                } else if (adj[i][k] > 0 && adj[k][j] > 0)
                    adj[i][j] = min(adj[i][j], adj[i][k] + adj[k][j]);
            }
        }
    }
    // show();
    for (int i = 1; i <= n; i++) {
        bool flag = true;
        for (int j = 1; j <= n; j++) {
            if (adj[i][j] == MAX) {
                flag = false;
                break;
            }
        }
        ans += flag;
    }
    cout << ans << endl;
}

int main() {
    FAST_IO
    int T = 1;
    for (int i = 0; i < T; i++) {
        solve();
    }
    return 0;
}
