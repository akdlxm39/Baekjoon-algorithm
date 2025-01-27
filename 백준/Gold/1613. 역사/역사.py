import sys
input = sys.stdin.readline

def main():
    n, k = map(int, input().split())
    next_event = [[0]*(n+1) for _ in range(n+1)]
    for _ in range(k):
        x, y = map(int, input().split())
        next_event[x][y] = -1
        next_event[y][x] = 1
    for k in range(1, n+1):
        for x in range(1, n+1):
            for y in range(1, n+1):
                if next_event[x][k] == -1 and next_event[k][y] == -1:
                    next_event[x][y] = -1
                elif next_event[x][k] == 1 and next_event[k][y] == 1:
                    next_event[x][y] = 1
    for _ in range(int(input())):
        x, y = map(int, input().split())
        print(next_event[x][y])

if __name__ == "__main__":
    main()