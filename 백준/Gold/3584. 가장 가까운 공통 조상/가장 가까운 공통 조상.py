import sys
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        parents = [0] * (n + 1)
        for _ in range(n - 1):
            a, b = map(int, input().split())
            parents[b] = a
        x, y = map(int, input().split())
        route = [False] * (n + 1)
        while x > 0:
            route[x] = True
            x = parents[x]
        while not route[y]:
            y = parents[y]
        print(y)

if __name__ == "__main__":
    main()