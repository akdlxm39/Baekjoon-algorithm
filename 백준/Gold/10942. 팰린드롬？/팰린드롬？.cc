// https://www.acmicpc.net/problem/10942 팰린드롬?
#include<bits/stdc++.h>
using namespace std;

int n, m, s, e;
vector<int> nums, palindromeRadius;

void solve() {
    cin >> n;
    nums.resize(n * 2 + 1, 0);
    for (int i = 0; i < n; ++i)
        cin >> nums[i * 2 + 1];
    nums[0] = -1, nums[n * 2] = -2;
    palindromeRadius.resize(n * 2 + 1, 0);
    for (int i = 1, c = 0, r = 0; i < 2 * n; ++i) {
        if (i < r)
            palindromeRadius[i] = min(r - i, palindromeRadius[2 * c - i]);
        while (nums[i - (palindromeRadius[i] + 1)] == nums[i + (palindromeRadius[i] + 1)])
            ++palindromeRadius[i];
        if (i + palindromeRadius[i] > r)
            c = i, r = i + palindromeRadius[i];
    }
    cin >> m;
    while (m--) {
        cin >> s >> e;
        cout << (palindromeRadius[s + e - 1] >= e - s ? "1\n" : "0\n");
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int t = 1;
    while (t--) solve();
    return 0;
}
