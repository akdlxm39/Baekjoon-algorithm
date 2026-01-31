#include <cstring>
#include <iostream>
#include <set>
#include <string>
using namespace std;

int ret, n, m, k;
string s;
set<string> passwords;

void input()
{
    passwords.clear();
    ret = 0;
    cin >> n >> k >> s;
    m = n / 4;
}

void solve()
{
    s += s.substr(0, m);
    for (int i = 0; i < n; ++i)
    {
        passwords.insert(s.substr(i, m));
    }
    auto it = passwords.end();
    while (k--)
        --it;
    ret = stoi(*it, nullptr, 16);
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int T = 1;
    cin >> T;
    for (int tc = 1; tc <= T; ++tc)
    {
        input();
        solve();
        cout << "#" << tc << " " << ret << '\n';
    }

    return 0;
}