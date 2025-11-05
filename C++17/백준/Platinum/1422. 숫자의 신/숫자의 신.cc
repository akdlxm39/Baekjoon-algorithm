// https://www.acmicpc.net/problem/1422 숫자의 신
#include<bits/stdc++.h>
using namespace std;

int n, k;
vector<string> nums;

bool cmp1(string &l, string &r) {
    if (l.length() == r.length())
        return l < r;
    return l.length() < r.length();
}

bool cmp2(string &l, string &r) {
    return l + r > r + l;
}

void solve() {
    cin >> k >> n;
    int x = n - k;
    nums.resize(k);
    for (string &s: nums) cin >> s;
    sort(nums.begin(), nums.end(), cmp2);
    auto max_iter = max_element(nums.begin(), nums.end(), cmp1);
    for (auto iter = nums.begin(); iter != nums.end(); ++iter) {
        cout << *iter;
        if (iter == max_iter)
            while (x--)
                cout << *iter;
    }
    cout << '\n';
}


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int t = 1;
    while (t--) solve();
    return 0;
}
