// https://www.acmicpc.net/problem/2631 줄세우기
#include<bits/stdc++.h>
using namespace std;

typedef long long ll;

int n;
vector<int> arr;

void solve() {
    cin >> n;
    int x;
    cin >> x;
    arr.push_back(x);
    for (int i = 1; i < n; i++) {
        cin >> x;
        if (arr.back() <= x)
            arr.push_back(x);
        else
            *lower_bound(arr.begin(), arr.end(), x) = x;
    }
    cout << n - arr.size() << '\n';
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
