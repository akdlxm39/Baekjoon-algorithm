import sys
input = sys.stdin.readline
modular = 1_000_000_007

def init(tree, node, left, right):
    if left == right:
        tree[node] = int(input())
        return
    mid = (left + right) // 2
    init(tree, node*2, left, mid)
    init(tree, node*2+1, mid+1, right)
    tree[node] = tree[node*2]*tree[node*2+1]%modular

def update(tree, node, left, right, idx, num):
    if left == right:
        tree[node] = num
        return
    mid = (left + right) // 2
    if left <= idx <= mid:
        update(tree, node*2, left, mid, idx, num)
    else:
        update(tree, node*2+1, mid+1, right, idx, num)
    tree[node] = tree[node*2]*tree[node*2+1]%modular

def get(tree, node, left, right, start, end):
    if end < left or right < start:
        return 1
    if start <= left and right <= end:
        return tree[node]
    mid = (left + right) // 2
    return (get(tree, node*2, left, mid, start, end) *
            get(tree, node*2+1, mid+1, right, start, end)
            % modular)

def main():
    n, m, k = map(int, input().split())
    tree = [0] * (n * 4)
    init(tree, 1, 1, n)
    for _ in range(m+k):
        a, b, c = map(int, input().split())
        if a == 1:
            update(tree, 1, 1, n, b, c)
        else:
            print(get(tree, 1, 1, n, b, c))

if __name__ == "__main__":
    main()