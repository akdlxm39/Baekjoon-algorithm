// https://www.acmicpc.net/problem/7662 이중 우선순위 큐
#include<bits/stdc++.h>
using namespace std;

const int MAX = 1'000'001;

priority_queue<int, vector<int>, greater<> > min_heap;
priority_queue<int> max_heap;
unordered_map<int, int> in_heap;
int k, x, heap_size;
char c;

void solve() {
    cin >> k;
    min_heap = priority_queue<int, vector<int>, greater<> >();
    max_heap = priority_queue<int>();
    in_heap.clear();
    heap_size = 0;
    while (k--) {
        cin >> c >> x;
        if (c == 'I') {
            min_heap.push(x);
            max_heap.push(x);
            ++in_heap[x];
            ++heap_size;
        } else {
            if (heap_size == 0) continue;
            if (x == 1) {
                while (true) {
                    int cur = max_heap.top();
                    max_heap.pop();
                    if (in_heap[cur]) {
                        --in_heap[cur];
                        --heap_size;
                        break;
                    }
                }
            } else {
                while (true) {
                    int cur = min_heap.top();
                    min_heap.pop();
                    if (in_heap[cur]) {
                        --in_heap[cur];
                        --heap_size;
                        break;
                    }
                }
            }
        }
    }
    if (heap_size) {
        while (in_heap[max_heap.top()] == 0)
            max_heap.pop();
        while (in_heap[min_heap.top()] == 0)
            min_heap.pop();
        cout << max_heap.top() << ' ' << min_heap.top() << '\n';
    } else
        cout << "EMPTY\n";
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int t = 1;
    cin >> t;
    while (t--) solve();
    return 0;
}
