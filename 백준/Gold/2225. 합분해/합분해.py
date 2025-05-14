import sys
input = sys.stdin.readline
divider = 1_000_000_000

def main():
    n, k = map(int, input().split())
    if k == 1:
        print(1)
        return
    memo = [0]*(k+1) ; memo[1] = 1
    for i in range(2, n+1):
        for j in range(min(k, i), 1, -1):
            memo[j] = (memo[j] + memo[j-1]) % divider
    ans, theta = 0, 1
    for i in range(1, k+1):
        theta = theta * (k-i+1) // i
        ans = (ans + memo[i] * theta) % divider
    print(ans)

if __name__ == "__main__":
    main()