// https://www.acmicpc.net/problem/1422 숫자의 신
#include<bits/stdc++.h>
using namespace std;

int n, k;
vector<pair<string, int> > nums;

bool cmp(pair<string, int> l, pair<string, int> r) {
    return l.first + r.first > r.first + l.first;
}

void solve() {
    cin >> k >> n;
    int max_len = -1;
    int max_idx = -1;
    for (int i = 0; i < k; ++i) {
        string x;
        cin >> x;
        nums.emplace_back(x, 1);
        int len = x.length();
        if (max_len < len) {
            max_len = len;
            max_idx = i;
        } else if (max_len == len && nums[max_idx].first < x) {
            max_idx = i;
        }
    }
    nums[max_idx].second += n - k;
    sort(nums.begin(), nums.end(), cmp);
    string ans;
    for (auto [x, cnt]: nums) {
        while (cnt--) cout << x;
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
