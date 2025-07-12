import sys
input = sys.stdin.readline

def update(n, tree, i):
    while i <= n:
        tree[i] += 1
        i += i & -i

def sum(tree, i):
    res = 0
    while i > 0:
        res += tree[i]
        i -= i & -i
    return res

def main():
    n = int(input())
    tmp = sorted(((int(input()), i) for i in range(n)), reverse=True)
    runner = [0] * n
    for i, (_, j) in enumerate(tmp, 1):
        runner[j] = i
    tree = [0] * (n+1)
    ans = [0] * n
    for i in range(n):
        ans[i] = sum(tree, runner[i]) + 1
        update(n, tree, runner[i])
    print('\n'.join(map(str, ans)))

if __name__ == "__main__":
    main()