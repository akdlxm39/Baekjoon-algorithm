import sys

input = sys.stdin.readline


def update(n, tree, idx):
    while idx <= n:
        tree[idx] += 1
        idx += idx & -idx


def range_sum(tree, idx):
    res = 0
    while idx > 0:
        res += tree[idx]
        idx -= idx & -idx
    return res


def main():
    n = int(input())
    nums = list(map(int, input().split()))
    tree = [0] * (n + 1)
    ans = 0
    for num in nums[::-1]:
        ans += range_sum(tree, num - 1)
        update(n, tree, num)
    print(ans)


if __name__ == "__main__":
    main()
