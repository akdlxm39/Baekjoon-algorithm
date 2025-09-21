// https://www.acmicpc.net/problem/20055 컨베이어 벨트 위의 로봇
#include<bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;

#define FAST_IO ios_base::sync_with_stdio(0);cin.tie(NULL);

void solve() {
    int n, k;
    cin >> n >> k;
    int s = 0, e = n - 1;
    n *= 2;
    vector<int> belt(n);
    for (int i = 0; i < n; i++) cin >> belt[i];
    deque<int> robots;
    int ans = 0;
    while (k > 0) {
        s = (s - 1 + n) % n;
        e = (e - 1 + n) % n;
        if (!robots.empty() && robots[0] == e) {
            robots.pop_front();
        }
        for (int i = 0; i < robots.size(); i++) {
            int nxt = (robots[i] + 1) % n;
            if (i == 0 || nxt != robots[i - 1]) {
                if (belt[nxt] > 0) {
                    robots[i] = nxt;
                    if (--belt[robots[i]] == 0) {
                        k--;
                    }
                }
            }
        }
        if (!robots.empty() && robots[0] == e) {
            robots.pop_front();
        }
        if (belt[s] > 0) {
            robots.push_back(s);
            if (--belt[s] == 0) {
                k--;
            }
        }
        ans++;
    }
    cout << ans << '\n';
}

int main() {
    FAST_IO
    int T = 1;
    for (int i = 0; i < T; i++) {
        solve();
    }
    return 0;
}
