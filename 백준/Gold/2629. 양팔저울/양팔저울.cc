// https://www.acmicpc.net/problem/2629 양팔저울
#include<bits/stdc++.h>
using namespace std;

const int MAX = 400001;
int n, x;
bool visited[MAX];
vector<int> weights;

void solve() {
    cin >> n;
    weights.push_back(0);
    while (n--) {
        cin >> x;
        int len = weights.size();
        for (int j = 0; j < len; ++j) {
            int tmp = weights[j] + x;
            if (tmp < MAX && !visited[tmp]) {
                weights.push_back(tmp);
                visited[tmp] = true;
            }
            int tmp2 = abs(weights[j] - x);
            if (!visited[tmp2]) {
                weights.push_back(tmp2);
                visited[tmp2] = true;
            }
        }
    }
    cin >> n;
    while (n--) {
        cin >> x;
        cout << (visited[x] ? "Y " : "N ");
    }
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
