// https://www.acmicpc.net/problem/11868 님 게임 2
#include<bits/stdc++.h>
using namespace std;

int n;

void solve() {
    cin >> n;
    int tmp = 0;
    for (int i = 0, x; i < n; ++i) {
        cin >> x;
        tmp ^= x;
    }
    cout << (tmp ? "koosaga\n" : "cubelover\n");
}


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int t = 1;
    while (t--) solve();
    return 0;
}
