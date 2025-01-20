import sys
input = sys.stdin.readline

def solve(x, size, k):
    if k == 0:
        return "moo"[x]
    m1 = size[k-1]
    m2 = m1 + k + 3
    if m2 <= x:
        return solve(x - m2, size, k - 1)
    elif x < m1:
        return solve(x, size, k - 1)
    elif m1 < x < m2:
        return "o"
    else:
        return "m"

# L(k) = 2 * L(K-1) + k + 3
# L(k) = 2^k * L(0) + sum(1~k) + 3*k

def main():
    n = int(input())
    k = 0
    size = [3]
    while size[-1] < n:
        size.append(2 * size[-1] + k + 4)
        k += 1
    print(solve(n-1, size, k))


if __name__ == "__main__":
    main()