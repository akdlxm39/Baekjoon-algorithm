import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def get_substrings(n):
    for i in range(1, len(str(n))+1):
        for j in range(i):
            tmp = (n%(10**i))//(10**j)
            if tmp != n and tmp != 0:
                yield tmp

    
def can_win(memo, n):
    if memo[n] is not None:
        return memo[n]
    for k in get_substrings(n):
        if not can_win(memo, n-k):
            memo[n] = True
            break
    else:
        memo[n] = False
    return memo[n]

def main():
    n = int(input())
    memo = [False]*(10) + [None]*(n-9)
    ans = 1000000
    for k in get_substrings(n):
        if not can_win(memo, n-k) and k < ans:
            ans = k
    print(ans if ans < 1000000 else -1)

if __name__ == "__main__":
    main()