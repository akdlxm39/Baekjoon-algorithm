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
        edges = [0] * (n+1)
        degrees = [0] * (n+1)
        for _ in range(m):
            a, b = map(int, input().split())
            if rank[a] < rank[b]:
                degrees[a] += 1
                edges[b] += 1
            else:
                degrees[b] += 1
                edges[a] += 1
        ans  = [0]*(n)
        for r, t in enumerate(ranking):
            nr = r + degrees[t] - edges[t]
            if 0 <= nr < n and ans[nr] == 0:
                ans[nr] = t
            else:
                print("IMPOSSIBLE")
                break
        else:
            print(*ans)

if __name__ == "__main__":
    main()