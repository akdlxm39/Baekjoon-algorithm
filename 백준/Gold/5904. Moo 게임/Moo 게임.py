import sys
input = sys.stdin.readline

def solve(x, l, size, k):
    if k == 0:
        return "moo"[x]
    m1 = size[k-1]
    m2 = m1 + k + 3
    if x == m1:
        return "m"
    elif m1 < x < m2:
        return "o"
    elif x < m1:
        return solve(x, l, size, k-1)
    else:
        return solve(x-m2, l+size[k-1], size, k-1)

# L(k) = 2 * L(K-1) + k + 3
# L(k) = 2^k * L(0) + sum(1~k) + 3*k

def main():
    n = int(input())
    l = k = 0
    size = [3]
    while size[-1] <= n:
        size.append(2 * size[-1] + k + 4)
        k += 1
    print(solve(n-1, l, size, k))


if __name__ == "__main__":
    main()

