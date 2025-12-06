// https://www.acmicpc.net/problem/10942 팰린드롬?
#include<bits/stdc++.h>
using namespace std;

int n, m, s, e;
vector<int> nums;
vector<vector<bool> > isPalindrome;

void solve() {
    cin >> n;
    nums.resize(n);
    for (auto &x: nums)
        cin >> x;
    isPalindrome.resize(n, vector<bool>(n, true));
    for (int k = 1; k < n; ++k) {
        for (int i = 0; i < n - k; ++i) {
            int j = i + k;
            isPalindrome[i][j] = nums[i] == nums[j] && isPalindrome[i + 1][j - 1];
        }
    }

    cin >> m;
    while (m--) {
        cin >> s >> e;
        cout << (isPalindrome[s - 1][e - 1] ? "1\n" : "0\n");
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int t = 1;
    while (t--) solve();
    return 0;
}
