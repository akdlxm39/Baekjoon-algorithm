// https://www.acmicpc.net/problem/2343 기타 레슨
#include<bits/stdc++.h>
using namespace std;

const int INF = 1'000'000'001;

int n, m;
vector<int> lesson;

bool check(int x) {
    int tmp = 0, cnt = 0;
    for (const int &l: lesson) {
        if (tmp + l <= x)
            tmp += l;
        else {
            ++cnt;
            tmp = l;
        }
    }
    return cnt < m;
}

void solve() {
    int left = 0, right = INF, ans = -1;
    cin >> n >> m;
    lesson.resize(n);
    for (int &l: lesson) {
        cin >> l;
        left = max(left, l);
    }
    while (left <= right) {
        int mid = (left + right) / 2;
        if (check(mid)) {
            ans = mid;
            right = mid - 1;
        } else
            left = mid + 1;
    }
    cout << ans << '\n';
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int t = 1;
    while (t--) solve();
    return 0;
}
