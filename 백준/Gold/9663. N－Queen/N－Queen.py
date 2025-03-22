import sys
input = sys.stdin.readline

def n_queen(N, i, cant):
    if i == N:
        return 1
    answer = 0
    for j in range(N):
        if cant[0][j] or cant[1][i+j] or cant[2][N-1+i-j]:
            continue
        cant[0][j] = cant[1][i+j] = cant[2][N-1+i-j] = True
        answer += n_queen(N, i + 1, cant)
        cant[0][j] = cant[1][i+j] = cant[2][N-1+i-j] = False
    return answer

def main():
    N = int(input())
    answer = n_queen(N, 0, [[False]*N, [False]*(2*N-1), [False]*(2*N-1)])
    print(answer)

main()