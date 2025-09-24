#include<bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;

#define FAST_IO ios_base::sync_with_stdio(0);cin.tie(NULL);
#define endl '\n';
int not_(int x) { return x % 2 ? x - 1 : x + 1; }

const int MAX = 20002;
int n, m;
int discovered[MAX], sccNumber[MAX], answer[MAX], cnt1, cnt2;
unordered_set<int> adj[MAX];
stack<int> st;
vector<vector<int> > scc;
vector<int> fix;

int dfs_scc(int cur) {
    discovered[cur] = cnt1++;
    int res = discovered[cur];
    st.push(cur);
    for (const int nxt: adj[cur]) {
        if (discovered[nxt] == -1)
            res = min(res, dfs_scc(nxt));
        else if (sccNumber[nxt] == -1)
            res = min(res, discovered[nxt]);
    }
    if (res == discovered[cur]) {
        vector<int> new_scc;
        while (true) {
            int tmp = st.top();
            st.pop();
            sccNumber[tmp] = cnt2;
            new_scc.push_back(tmp);
            if (tmp == cur) break;
        }
        scc.push_back(new_scc);
        ++cnt2;
    }
    return res;
}

void make_scc() {
    memset(discovered, -1, sizeof(discovered));
    memset(sccNumber, -1, sizeof(sccNumber));
    cnt1 = 0, cnt2 = 0;
    st = stack<int>();
    for (int i = 2; i < 2 * n + 2; ++i) {
        if (discovered[i] == -1)
            dfs_scc(i);
    }
}


void solve() {
    cin >> n >> m;
    memset(answer, -1, sizeof(answer));
    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        u = u > 0 ? 2 * u + 1 : -2 * u;
        v = v > 0 ? 2 * v + 1 : -2 * v;
        adj[not_(u)].insert(v);
        adj[not_(v)].insert(u);
    }
    make_scc();
    for (int i = 1; i <= n; ++i) {
        if (sccNumber[i * 2] == sccNumber[i * 2 + 1]) {
            cout << 0 << endl;
            return;
        }
    }
    for (const auto &s: scc) {
        for (int cur: s) {
            if (answer[cur / 2] != -1) continue;
            answer[cur / 2] = cur % 2;
        }
    }
    cout  << 1 << endl;
    for (int i = 1; i <= n; ++i) {
        cout << answer[i] << ' ';
    }
}

int main() {
    FAST_IO
    int T = 1;
    for (int i = 0; i < T; i++) {
        solve();
    }
    return 0;
}
