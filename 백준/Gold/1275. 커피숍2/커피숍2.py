import sys
input = sys.stdin.readline

def update(n, tree, idx, num):
    while idx <= n:
        tree[idx] += num
        idx += idx & -idx

def sum(tree, left, right):
    res = 0
    while 0 < right:
        res += tree[right]
        right -= right & -right
    left -= 1
    while 0 < left:
        res -= tree[left]
        left -= left & -left
    return res

def main():
    n, q = map(int, input().split())
    nums = [0] + list(map(int, input().split()))
    tree = [0] * (n + 1)
    for i in range(1, n+1):
        update(n, tree, i, nums[i])
    for _ in range(q):
        x, y, a, b = map(int, input().split())
        if x > y:
            x, y = y, x
        print(sum(tree, x, y))
        gap = b - nums[a]
        nums[a] = b
        update(n, tree, a, gap)

if __name__ == "__main__":
    main()