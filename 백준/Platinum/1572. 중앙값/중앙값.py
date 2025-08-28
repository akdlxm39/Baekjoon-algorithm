import sys
from collections import deque

input = sys.stdin.readline

def update(tree, node, left, right, idx, delta):
    tree[node] += delta
    if left == right:
        return
    mid = (left + right) // 2
    if left <= idx <= mid:
        update(tree, node * 2, left, mid, idx, delta)
    else:
        update(tree, node * 2 + 1, mid + 1, right, idx, delta)

def find_median(tree, node, left, right, m):
    if left == right:
        return left
    mid = (left + right) // 2
    if tree[node * 2] >= m:
        return find_median(tree, node * 2, left, mid, m)
    else:
        return find_median(tree, node * 2 + 1, mid + 1, right, m - tree[node * 2])

def main():
    n, k = map(int, input().split())
    m = (k + 1) // 2
    nums = deque()
    tree = [0] * 262144
    ans = 0
    for i in range(k - 1):
        num = int(input())
        nums.append(num)
        update(tree, 1, 0, 65536, num, 1)
    for i in range(k - 1, n):
        num = int(input())
        nums.append(num)
        update(tree, 1, 0, 65536, num, 1)
        ans += find_median(tree, 1, 0, 65536, m)
        update(tree, 1, 0, 65536, nums.popleft(), -1)
    print(ans)

if __name__ == "__main__":
    main()
