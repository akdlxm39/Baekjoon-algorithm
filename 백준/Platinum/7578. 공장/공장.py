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
    mapping = {m:i for i, m in enumerate(map(int, input().split()), 1)}
    list = [mapping[m] for m in map(int, input().split())]
    tree = [0] * (n + 1)
    ans = 0
    for i in reversed(list):
        ans += sum(tree, i)
        update(n, tree, i)
    print(ans)

if __name__ == "__main__":
    main()