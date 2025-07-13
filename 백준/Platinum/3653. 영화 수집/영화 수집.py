import sys
input = sys.stdin.readline

def init(m, size, tree):
    for d in range(m+1, size+1):
        while d <= size:
            tree[d] += 1
            d += d & -d

def update(size, tree, i, j):
    while i <= size:
        tree[i] += 1
        i += i & -i
    while j <= size:
        tree[j] -= 1
        j += j & -j

def sum(tree, i):
    res = 0
    while i > 0:
        res += tree[i]
        i -= i & -i
    return res

def main():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        size = n + m
        dvd = list(range(m, size + 1))
        tree = [0] * (size + 1)
        init(m, size, tree)
        idx = m
        ans = []
        watch = map(int, input().split())
        for w in watch:
            ans.append(sum(tree, dvd[w] - 1))
            update(size, tree, idx, dvd[w])
            dvd[w] = idx
            idx -= 1
        print(' '.join(map(str, ans)))

if __name__ == "__main__":
    main()