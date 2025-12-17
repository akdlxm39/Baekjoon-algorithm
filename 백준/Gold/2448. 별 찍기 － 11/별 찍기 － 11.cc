// https://www.acmicpc.net/problem/2448 별 찍기 - 11
#include<bits/stdc++.h>
using namespace std;

int n, k;

void solve() {
    cin >> n;
    for (int i = 0; i < n; ++i) {
        vector<int> stars;
        if (i % 3 == 0)
            stars.push_back(n - i);
        else if (i % 3 == 1) {
            stars.push_back(n - i);
            stars.push_back(n - i + 2);
        } else {
            for (int j = n - i; j < n - i + 5; ++j)
                stars.push_back(j);
        }
        for (int a = i / 3, b = 6; a > 0; a /= 2, b *= 2) {
            if (a & 1) {
                int size = stars.size();
                for (int j = 0; j < size; ++j)
                    stars.push_back(stars[j] + b);
            }
        }

        int c = 1;
        for (auto &star: stars) {
            for (; c < star; ++c)
                cout << ' ';
            if (c++ == star)
                cout << '*';
        }
        if (i < n - 1) {
            for (; c < n * 2 + 1; ++c)
                cout << ' ';
            cout << '\n';
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int t = 1;
    while (t--) solve();
    return 0;
}
