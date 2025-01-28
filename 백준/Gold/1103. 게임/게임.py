import sys
sys.setrecursionlimit(2505)
input = sys.stdin.readline

def solve(board, visited, moves, x, y, count):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    l = int(board[x][y])
    moves[x][y] = 1
    for dx, dy in directions:
        nx, ny = x + dx * l, y + dy * l
        if not (0 <= nx < len(board) and 0 <= ny < len(board[0])) or board[nx][ny] == 'H':
            continue
        elif visited[nx][ny] == 1:
            return False
        elif visited[nx][ny] == 0:
            visited[nx][ny] = 1
            if not solve(board, visited, moves, nx, ny, count + 1):
                return False
            visited[nx][ny] = 2
        moves[x][y] = max(moves[x][y], moves[nx][ny]+1)
    return True

def main():
    n, m = map(int, input().split())
    board = [list(input().rstrip()) for _ in range(n)]
    visited = [[0]*m for _ in range(n)]
    visited[0][0] = 1
    moves = [[0]*m for _ in range(n)]
    if solve(board, visited, moves, 0, 0, 1):
        print(moves[0][0])
    else:
        print(-1)

if __name__ == "__main__":
    main()