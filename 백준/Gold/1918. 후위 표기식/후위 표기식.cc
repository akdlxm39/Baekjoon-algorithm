// https://www.acmicpc.net/problem/1918 후위 표기식
#include<bits/stdc++.h>
using namespace std;

string expr;
stack<char> st;
vector<char> ans;

void solve() {
    cin >> expr;
    for (auto &x: expr) {
        if (x == '(') {
            st.push(x);
        } else if (x == '*' || x == '/') {
            while (!st.empty() && st.top() != '(' && st.top() != '+' && st.top() != '-') {
                ans.push_back(st.top());
                st.pop();
            }
            st.push(x);
        } else if (x == '+' || x == '-') {
            while (!st.empty() && st.top() != '(') {
                ans.push_back(st.top());
                st.pop();
            }
            st.push(x);
        } else if (x == ')') {
            while (st.top() != '(') {
                ans.push_back(st.top());
                st.pop();
            }
            st.pop();
        } else
            ans.push_back(x);
    }
    while (!st.empty()) {
        ans.push_back(st.top());
        st.pop();
    }
    for (auto &x: ans)
        cout << x;
    cout << '\n';
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int t = 1;
    while (t--) solve();
    return 0;
}
