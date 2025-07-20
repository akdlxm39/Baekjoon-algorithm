import sys
input = sys.stdin.readline

def update(n, tree, idx, delta):
    while idx <= n:
        tree[idx] += delta
        idx += idx & -idx

def range_sum(tree, left, right):
    res = 0
    while 0 < right:
        res += tree[right]
        right -= right & -right
    while 0 < left:
        res -= tree[left]
        left -= left & -left
    return res

def main():
    n, m = map(int, input().split())
    nums = [0] * (n + 1)
    tree = [0] * (n + 1)
    ans = []
    for _ in range(m):
        a, b, c = map(int, input().split())
        if a == 0:
            if c < b:
                b, c = c, b
            ans.append(range_sum(tree, b - 1, c))
        else:
            delta = c - nums[b]
            nums[b] = c
            update(n, tree, b, delta)
    print('\n'.join(map(str, ans)))

if __name__ == "__main__":
    main()