import sys
input = sys.stdin.readline

def solve(events, cur, visited):
    visited[cur] = True
    l = list(events[cur])
    for nxt in l:
        if not visited[nxt]:
            solve(events, nxt, visited)
        events[cur] |= events[nxt]

def main():
    n, k = map(int, input().split())
    events = [set() for _ in range(n+1)]
    for _ in range(k):
        x, y = map(int, input().split())
        events[x].add(y)
    visited = [False] * (n + 1)
    for i in range(1, n + 1):
        solve(events, i, visited)
    for _ in range(int(input())):
        x, y = map(int, input().split())
        if y in events[x]:
            print(-1)
        elif x in events[y]:
            print(1)
        else:
            print(0)

if __name__ == "__main__":
    main()