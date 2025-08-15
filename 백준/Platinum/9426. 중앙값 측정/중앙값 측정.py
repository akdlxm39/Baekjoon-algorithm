import sys
from collections import deque

input = sys.stdin.readline


def add(tree, node, left, right, num):
    tree[node] += 1
    if left == right: return
    mid = (left + right) // 2
    if left <= num <= mid:
        add(tree, node * 2, left, mid, num)
    else:
        add(tree, node * 2 + 1, mid + 1, right, num)


def subtract(tree, node, left, right, num):
    tree[node] -= 1
    if left == right: return
    mid = (left + right) // 2
    if left <= num <= mid:
        subtract(tree, node * 2, left, mid, num)
    else:
        subtract(tree, node * 2 + 1, mid + 1, right, num)


def get_median(tree, node, left, right, cnt):
    if left == right: return left
    mid = (left + right) // 2
    if tree[node * 2] >= cnt:
        return get_median(tree, node * 2, left, mid, cnt)
    else:
        return get_median(tree, node * 2 + 1, mid + 1, right, cnt - tree[node * 2])


def main():
    n, k = map(int, input().split())
    median_k = (k + 1) // 2
    tree = [0] * (2 ** 17)
    queue = deque()
    for _ in range(k):
        num = int(input())
        add(tree, 1, 0, 65535, num)
        queue.append(num)
    ans = get_median(tree, 1, 0, 65535, median_k)
    for _ in range(n - k):
        num = int(input())
        subtract(tree, 1, 0, 65535, queue.popleft())
        add(tree, 1, 0, 65535, num)
        queue.append(num)
        ans += get_median(tree, 1, 0, 65535, median_k)
    print(ans)


if __name__ == "__main__":
    main()
