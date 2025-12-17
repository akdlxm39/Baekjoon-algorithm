// https://www.acmicpc.net/problem/2467 용액
#include<bits/stdc++.h>
using namespace std;

vector<int> nums;
int n, l, r, ans = 2'000'000'001, ans_l, ans_r;

void solve() {
    cin >> n;
    nums.resize(n);
    for (auto &x: nums)
        cin >> x;
    l = 0, r = n - 1;
    while (l < r) {
        if (ans > abs(nums[l] + nums[r]))
            ans = abs((ans_l = nums[l]) + (ans_r = nums[r]));
        nums[l] + nums[r] < 0 ? ++l : --r;
    }
    cout << ans_l << ' ' << ans_r << '\n';
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int t = 1;
    while (t--) solve();
    return 0;
}
