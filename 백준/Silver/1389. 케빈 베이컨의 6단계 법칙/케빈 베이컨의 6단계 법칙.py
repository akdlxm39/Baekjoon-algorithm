import sys
input = sys.stdin.readline
INF = int(1e9)

def main():
    n, m = map(int, input().split())
    adj_list = [[INF]*(n+1) for _ in range(n+1)]
    for i in range(1, n+1):
        adj_list[i][i] = 0
    for _ in range(m):
        a, b = map(int, input().split())
        adj_list[a][b] = 1
        adj_list[b][a] = 1
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                tmp = adj_list[i][k] + adj_list[k][j]
                if tmp < adj_list[i][j]:
                    adj_list[i][j] = tmp
    
    ans, ans_bacon = 0, INF
    for cur in range(1, n+1):
        cur_bacon = sum(adj_list[cur][1:])
        if cur_bacon < ans_bacon:
            ans = cur
            ans_bacon = cur_bacon
    print(ans)

if __name__ == "__main__":
    main()