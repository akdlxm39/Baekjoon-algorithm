import sys
input = sys.stdin.readline

def main():
    n, k = map(int, input().split())
    events = [[0]*(n+1) for _ in range(n+1)]
    for _ in range(k):
        x, y = map(int, input().split())
        events[x][y] = 1
    for k in range(1, n+1):
        for x in range(1, n+1):
            for y in range(1, n+1):
                if events[x][k] and events[k][y]:
                    events[x][y] = 1
    for _ in range(int(input())):
        x, y = map(int, input().split())
        if events[x][y]:
            print(-1)
        elif events[y][x]:
            print(1)
        else:
            print(0)

if __name__ == "__main__":
    main()