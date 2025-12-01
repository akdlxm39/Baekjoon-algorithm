// https://www.acmicpc.net/problem/5639 이진 검색 트리
#include<bits/stdc++.h>
using namespace std;

struct Node {
    int value = 0;
    Node *left = nullptr, *right = nullptr;
    Node(int v) : value(v) { ; }

    void push(Node *new_node) {
        if (new_node->value < value) {
            if (left == nullptr)
                left = new_node;
            else
                left->push(new_node);
        } else {
            if (right == nullptr)
                right = new_node;
            else
                right->push(new_node);
        }
    }

    void show() {
        if (left) left->show();
        if (right) right->show();
        cout << value << '\n';
    }
} root(0);

void solve() {
    int x;
    while (cin >> x)
        root.push(new Node(x));
    root.right->show();
}


int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int t = 1;
    while (t--) solve();
    return 0;
}
