import sys
input = sys.stdin.readline
INF = int(1e9)

def main():
    n, m = int(input()), int(input())
    adj_matrix = [[INF]*n for _ in range(n)]
    for i in range(n):
        adj_matrix[i][i] = 0
    for _ in range(m):
        s, e, cost = map(int, input().split())
        if adj_matrix[s-1][e-1] > cost:
            adj_matrix[s-1][e-1] = cost
    for k in range(n):
        for i in range(n):
            for j in range(n):
                tmp = adj_matrix[i][k] + adj_matrix[k][j]
                if adj_matrix[i][j] > tmp:
                    adj_matrix[i][j] = tmp
    for line in adj_matrix:
        print(' '.join(map(lambda x: str(x) if x != INF else '0', line)))

if __name__ == "__main__":
    main()