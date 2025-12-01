// https://www.acmicpc.net/problem/5639 이진 검색 트리
#include<bits/stdc++.h>
using namespace std;

typedef vector<int>::iterator vi;

vector<int> v, ans;

void postorder(vi begin, vi end) {
    if (begin >= end)
        return;
    vi middle = upper_bound(begin, end, *begin);
    postorder(begin + 1, middle);
    postorder(middle, end);
    cout << *begin << '\n';
}

void solve() {
    int x;
    while (cin >> x)
        v.push_back(x);
    postorder(v.begin(), v.end());
}


int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int t = 1;
    while (t--) solve();
    return 0;
}
