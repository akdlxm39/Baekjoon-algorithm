// https://www.acmicpc.net/problem/17299 오등큰수
#include<bits/stdc++.h>
using namespace std;


vector<int> arr, ans;
stack<int> st;
int n, counter[1'000'001];


void solve() {
    cin >> n;
    for (int i = 0, x; i < n; i++) {
        cin >> x;
        arr.push_back(x);
        counter[x]++;
    }
    for (auto cur = arr.rbegin(); cur != arr.rend(); ++cur) {
        while (!st.empty() && counter[*cur] >= counter[st.top()])
            st.pop();
        if (st.empty()) ans.push_back(-1);
        else ans.push_back(st.top());
        st.push(*cur);
    }
    for (auto cur = ans.rbegin(); cur != ans.rend(); ++cur)
        cout << *cur << " ";
}


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int t = 1;
    while (t--)
        solve();
    return 0;
}
