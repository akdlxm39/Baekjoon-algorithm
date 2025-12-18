// https://www.acmicpc.net/problem/12851 숨바꼭질 2
#include<bits/stdc++.h>
using namespace std;

const int MAX = 100'001, INF = 999'999;

int n, m, visited[MAX], timer[MAX], ans_time, ans_cnt;

void solve() {
    fill(visited, visited + MAX, 0);
    fill(timer, timer + MAX, INF);
    cin >> n >> m;
    if (n == m) {
        cout << "0\n1";
        return;
    }
    queue<int> a, b;
    a.push(n);
    visited[n] = 1;
    timer[n] = 0;
    b.push(m);
    visited[m] = -1;
    timer[m] = 1;
    while (!a.empty() || !b.empty()) {
        queue<int> nxt_a, nxt_b;
        while (!a.empty()) {
            int cur = a.front();
            a.pop();
            if (cur > 0) {
                if (visited[cur - 1] < 0) {
                    ans_time = timer[cur] + timer[cur - 1];
                    ans_cnt -= visited[cur] * visited[cur - 1];
                } else if (timer[cur] < timer[cur - 1]) {
                    timer[cur - 1] = timer[cur] + 1;
                    if (visited[cur - 1] == 0)
                        nxt_a.push(cur - 1);
                    visited[cur - 1] += visited[cur];
                }
            }
            if (cur < 100'000) {
                if (visited[cur + 1] < 0) {
                    ans_time = timer[cur] + timer[cur + 1];
                    ans_cnt -= visited[cur] * visited[cur + 1];
                } else if (timer[cur] < timer[cur + 1]) {
                    timer[cur + 1] = timer[cur] + 1;
                    if (visited[cur + 1] == 0)
                        nxt_a.push(cur + 1);
                    visited[cur + 1] += visited[cur];
                }
            }
            if (cur <= 50'000) {
                if (visited[cur * 2] < 0) {
                    ans_time = timer[cur] + timer[cur * 2];
                    ans_cnt -= visited[cur] * visited[cur * 2];
                } else if (timer[cur] < timer[cur * 2]) {
                    timer[cur * 2] = timer[cur] + 1;
                    if (visited[cur * 2] == 0)
                        nxt_a.push(cur * 2);
                    visited[cur * 2] += visited[cur];
                }
            }
        }
        a = nxt_a;
        if (ans_time) break;
        while (!b.empty()) {
            int cur = b.front();
            b.pop();
            if (cur > 0) {
                if (visited[cur - 1] > 0) {
                    ans_time = timer[cur] + timer[cur - 1];
                    ans_cnt -= visited[cur] * visited[cur - 1];
                } else if (timer[cur] < timer[cur - 1]) {
                    timer[cur - 1] = timer[cur] + 1;
                    if (visited[cur - 1] == 0)
                        nxt_b.push(cur - 1);
                    visited[cur - 1] += visited[cur];
                }
            }
            if (cur < 100'000) {
                if (visited[cur + 1] > 0) {
                    ans_time = timer[cur] + timer[cur + 1];
                    ans_cnt -= visited[cur] * visited[cur + 1];
                } else if (timer[cur] < timer[cur + 1]) {
                    timer[cur + 1] = timer[cur] + 1;
                    if (visited[cur + 1] == 0)
                        nxt_b.push(cur + 1);
                    visited[cur + 1] += visited[cur];
                }
            }
            if (cur && cur % 2 == 0) {
                if (visited[cur / 2] > 0) {
                    ans_time = timer[cur] + timer[cur / 2];
                    ans_cnt -= visited[cur] * visited[cur / 2];
                } else if (timer[cur] < timer[cur / 2]) {
                    timer[cur / 2] = timer[cur] + 1;
                    if (visited[cur / 2] == 0)
                        nxt_b.push(cur / 2);
                    visited[cur / 2] += visited[cur];
                }
            }
        }
        b = nxt_b;
        if (ans_time) break;
    }
    cout << ans_time << '\n' << ans_cnt << '\n';
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int t = 1;
    while (t--) solve();
    return 0;
}
