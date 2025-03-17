import sys
input = sys.stdin.readline

def shuffle(k, matrix, opers, used, cnt):
    if cnt == k:
        return min(sum(line) for line in matrix)
    ans = 5001
    for i in range(k):
        if used[i]:
            continue
        used[i] = True
        ans = min(ans, shuffle(k, rotation(matrix, *opers[i]), opers, used, cnt+1))
        used[i] = False
    return ans

def rotation(matrix, r, c, s):
    new_matrix = [row[:] for row in matrix]
    for d in range(1, s+1):
        x, y = r-1-d, c-1-d
        for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
            for _ in range(2*d):
                x, y, px, py = x + dx, y + dy, x, y
                new_matrix[x][y] = matrix[px][py]
    return new_matrix
    
def main():
    n, m, k = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    opers = [list(map(int, input().split())) for _ in range(k)]
    used = [False]*k
    ans = shuffle(k, matrix, opers, used, 0)
    print(ans)

if __name__ == "__main__":
    main()