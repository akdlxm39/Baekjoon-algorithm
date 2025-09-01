import sys

input = sys.stdin.readline
INF = int(1e9)


def bellman_ford(n, edges):
    dist = [INF] * (n + 1)
    dist[1] = 0
    for i in range(n - 1):
        for cur, nxt, cost in edges:
            if dist[cur] != INF:
                dist[nxt] = min(dist[nxt], dist[cur] + cost)
    for cur, nxt, cost in edges:
        if dist[cur] != INF and dist[nxt] > dist[cur] + cost:
            return -1
    return '\n'.join(map(lambda x: str(x) if x != INF else '-1', dist[2:]))


def main():
    n, m = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(m)]
    print(bellman_ford(n, edges))


if __name__ == "__main__":
    main()
