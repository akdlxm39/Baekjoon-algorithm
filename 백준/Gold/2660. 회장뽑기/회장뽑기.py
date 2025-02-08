import sys
input = sys.stdin.readline
INF = 987654321

def main():
    n = int(input())
    friendship = [[0 if i == j or i == 0 or j == 0 else INF for j in range(n+1)] for i in range(n+1)]
    while True:
        a, b = map(int, input().split())
        if a == -1:
            break
        friendship[a][b] = friendship[b][a] = 1
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                if friendship[i][k] == INF or friendship[k][j] == INF:
                    continue
                friendship[i][j] = min(friendship[i][j], friendship[i][k] + friendship[k][j])
    point = [max(f) for f in friendship[1:]]
    min_point = min(point)
    candidate = [i for i, x in enumerate(point, 1) if x == min_point]
    print(min_point, len(candidate))
    print(*candidate)

if __name__ == "__main__":
    main()