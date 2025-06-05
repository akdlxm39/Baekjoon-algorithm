import sys
input = sys.stdin.readline

def show(tree):
    i = d = 1
    while len(tree) > i+d:
        print(tree[i:i+d])
        i += d ; d *= 2

def init(tree, node, left, right):
    if left == right:
        tree[node] = int(input())
    else:
        mid = (left + right) // 2
        tree[node] = init(tree, node*2, left, mid) + init(tree, node*2+1, mid+1, right)
    return tree[node]

def lazy_update(tree, lazy, node, length):
    if lazy[node] == 0:
        return
    tree[node] += lazy[node] * length
    if length > 1:
        lazy[node*2] += lazy[node]
        lazy[node*2+1] += lazy[node]
    lazy[node] = 0

def update(tree, lazy, node, left, right, start, end, num):
    lazy_update(tree, lazy, node, right-left+1)
    if end < left or right < start:
        return 0
    if start <= left and right <= end:
        tree[node] += num * (right-left+1)
        if left < right:
            lazy[node*2] += num
            lazy[node*2+1] += num
        return num * (right-left+1)
    else:
        mid = (left + right) // 2
        tmp = update(tree, lazy, node*2, left, mid, start, end, num)
        tmp += update(tree, lazy, node*2+1, mid+1, right, start, end, num)
        tree[node] += tmp
        return tmp

def range_sum(tree, lazy, node, left, right, start, end):
    lazy_update(tree, lazy, node, right-left+1)
    if end < left or right < start:
        return 0
    if start <= left and right <= end:
        return tree[node]
    mid = (left + right) // 2
    return (range_sum(tree, lazy, node*2, left, mid, start, end)+
            range_sum(tree, lazy, node*2+1, mid+1, right, start, end))

def main():
    n, m, k = map(int, input().split())
    tree = [0]*(n*4)
    init(tree, 1, 1, n)
    lazy = [0]*(n*4)
    for _ in range(m+k):
        command = tuple(map(int, input().split()))
        if command[0] == 1:
            s, e, num = command[1:]
            update(tree, lazy, 1, 1, n, s, e, num)
        if command[0] == 2:
            s, e = command[1:]
            print(range_sum(tree, lazy, 1, 1, n, s, e))

if __name__ == "__main__":
    main()