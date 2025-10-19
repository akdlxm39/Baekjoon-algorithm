// https://www.acmicpc.net/problem/2873 롤러코스터
#include<bits/stdc++.h>
using namespace std;

int r, c;
string ans;

string make_ans(int ii, int jj) {
    string ret = "";
    bool toggle = true;
    for (int i = 0; i < r / 2; i++) {
        if (i != ii / 2) {
            for (int j = 1; j < c; j++)
                ret += toggle ? "R" : "L";
            ret += "D";
            for (int j = 1; j < c; j++)
                ret += toggle ? "L" : "R";
        } else {
            for (int j = 0; j < c / 2; j++) {
                if (j != jj / 2) {
                    ret += toggle ? "DRU" : "URD";
                } else {
                    ret += ii % 2 == 1 ? "RD" : "DR";
                    toggle = false;
                }
                if (j != c / 2 - 1)
                    ret += "R";
            }
        }
        if (i != r / 2 - 1)
            ret += "D";
    }
    return ret;
}

void solve() {
    cin >> r >> c;
    if (r % 2 == 1) {
        for (int i = 0; i < r; i++) {
            if (i % 2 == 0)
                for (int j = 1; j < c; j++)
                    ans += "R";
            else
                for (int j = 1; j < c; j++)
                    ans += "L";
            if (i != r - 1)
                ans += "D";
        }
    } else if (c % 2 == 1) {
        for (int i = 0; i < c; i++) {
            if (i % 2 == 0)
                for (int j = 1; j < r; j++)
                    ans += "D";
            else
                for (int j = 1; j < r; j++)
                    ans += "U";
            if (i != c - 1)
                ans += "R";
        }
    } else if (r == 2 && c == 2) {
        int a, b;
        cin >> a >> a >> b;
        ans = a < b ? "DR" : "RD";
    } else {
        int a, min_ = 1001, ii, jj;
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                cin >> a;
                if ((i + j) % 2 == 1 && a < min_) {
                    min_ = a;
                    ii = i;
                    jj = j;
                }
            }
        }
        ans = make_ans(ii, jj);
    }
    cout << ans << '\n';
}


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int t = 1;
    while (t--)
        solve();
    return 0;
}
