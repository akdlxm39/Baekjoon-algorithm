// https://www.acmicpc.net/problem/2467 용액
#include<bits/stdc++.h>
using namespace std;

vector<int> acid, alcali;
int n, x, ans = 2'000'000'001, a, b;

void solve() {
    cin >> n;
    while (n--) {
        cin >> x;
        if (x > 0)
            acid.push_back(x);
        else
            alcali.push_back(x);
    }
    sort(acid.begin(), acid.end());
    sort(alcali.rbegin(), alcali.rend());
    if (acid.size() >= 2 && ans > acid[0] + acid[1])
        ans = (a = acid[0]) + (b = acid[1]);
    if (alcali.size() >= 2 && ans > -alcali[0] - alcali[1])
        ans = -(b = alcali[0]) - (a = alcali[1]);
    auto acid_iter = acid.begin(), alcali_iter = alcali.begin();
    while (acid_iter != acid.end() && alcali_iter != alcali.end()) {
        int cur = *acid_iter + *alcali_iter;
        if (cur > 0) {
            if (ans > cur) {
                ans = cur;
                a = *alcali_iter;
                b = *acid_iter;
            }
            ++alcali_iter;
        } else {
            if (ans > -cur) {
                ans = -cur;
                a = *alcali_iter;
                b = *acid_iter;
            }
            ++acid_iter;
        }
    }
    cout << a << ' ' << b << '\n';
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int t = 1;
    while (t--) solve();
    return 0;
}
