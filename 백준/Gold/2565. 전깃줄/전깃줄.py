import sys
input = sys.stdin.readline

def main():
    N = int(input())
    get = [x for _,x in sorted(tuple(map(int,input().split())) for _ in range(N))]
    dp = [1] * N
    for i in range(1, N):
        dp[i] = 1 + max([0] + [dp[j] for j in range(i) if get[j]<get[i]])
    print(N - max(dp))
    
main()