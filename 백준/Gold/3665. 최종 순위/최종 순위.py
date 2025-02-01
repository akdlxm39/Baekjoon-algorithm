import sys
input = sys.stdin.readline

def main():
    T = int(input())
    for _ in range(T):
        n = int(input())
        ranking = list(map(int, input().split()))
        rank = [0] * (n+1)
        for i, r in enumerate(ranking):
            rank[r] = i
        m = int(input())
        gamma = [0] * (n+1)
        for _ in range(m):
            a, b = map(int, input().split())
            if rank[a] < rank[b]:
                gamma[a] += 1
                gamma[b] -= 1
            else:
                gamma[b] += 1
                gamma[a] -= 1
        ans  = [0]*(n)
        for r, t in enumerate(ranking):
            nr = r + gamma[t]
            if 0 <= nr < n and ans[nr] == 0:
                ans[nr] = t
            else:
                print("IMPOSSIBLE")
                break
        else:
            print(*ans)

if __name__ == "__main__":
    main()