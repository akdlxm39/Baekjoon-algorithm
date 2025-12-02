// https://www.acmicpc.net/problem/7662 이중 우선순위 큐
#include<bits/stdc++.h>
using namespace std;

template<typename T>
class DoubleEndedPriorityQueue {
    vector<T> heap;

public:
    DoubleEndedPriorityQueue() : heap(2) { heap.reserve(1'000'100); }
    ~DoubleEndedPriorityQueue() { ; }

    void push(const T &node) {
        size_t cur = heap.size();
        heap.push_back(node);
        if (cur & 1 && heap[cur] < heap[cur - 1])
            swap(heap[cur], heap[cur - 1]), --cur;
        while (cur > 3) {
            if (heap[cur] < heap[cur / 4 * 2])
                swap(heap[cur], heap[cur / 4 * 2]), cur = cur / 4 * 2;
            else if (heap[cur / 4 * 2 + 1] < heap[cur])
                swap(heap[cur], heap[cur / 4 * 2 + 1]), cur = cur / 4 * 2 + 1;
            else break;
        }
        heap[cur] = node;
    }

    void pop_min() {
        if (empty()) return;
        size_t cur = 2;
        swap(heap[cur], heap.back()), heap.pop_back();
        while (cur * 2 < heap.size()) {
            size_t nxt = cur * 2;
            if (nxt + 2 < heap.size() && heap[nxt + 2] < heap[nxt])
                nxt += 2;
            if (heap[nxt] < heap[cur]) {
                swap(heap[cur], heap[nxt]), cur = nxt;
                if (cur + 1 < heap.size() && heap[cur + 1] < heap[cur])
                    swap(heap[cur], heap[cur + 1]);
            } else break;
        }
    }

    void pop_max() {
        if (empty()) return;
        if (heap.size() == 3) {
            heap.pop_back();
            return;
        }
        size_t cur = 3;
        swap(heap[cur], heap.back()), heap.pop_back();
        while (cur * 2 - 1 < heap.size()) {
            size_t nxt = cur * 2 - 1;
            if (nxt + 2 < heap.size() && heap[nxt] < heap[nxt + 2])
                nxt += 2;
            if (heap[cur] < heap[nxt]) {
                swap(heap[cur], heap[nxt]), cur = nxt;
                if (heap[cur] < heap[cur - 1])
                    swap(heap[cur], heap[cur - 1]);
            } else break;
        }
    }

    T &top_min() { return heap[2]; }
    T &top_max() { return heap.size() > 3 ? heap[3] : heap[2]; }
    size_t size() { return heap.size() - 2; }
    bool empty() { return heap.size() == 2; }
    void clear() { heap.resize(2); }
};

int n, x;
char c;
DoubleEndedPriorityQueue<int> depq;

void solve() {
    cin >> n;
    depq.clear();
    while (n--) {
        cin >> c >> x;
        if (c == 'I')
            depq.push(x);
        else {
            if (x == 1) depq.pop_max();
            else depq.pop_min();
        }
    }
    if (depq.empty()) cout << "EMPTY\n";
    else cout << depq.top_max() << ' ' << depq.top_min() << '\n';
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int t = 1;
    cin >> t;
    while (t--) solve();
    return 0;
}
