import sys

input = sys.stdin.readline
INF = int(1e9)


def bellman_ford(n, edges):
    dist = [INF] * (n + 1)
    dist[1] = 0
    for _ in range(n - 1):
        for cur in range(1, n + 1):
            if dist[cur] == INF: continue
            for nxt, cost in edges[cur]:
                if dist[nxt] > dist[cur] + cost:
                    dist[nxt] = dist[cur] + cost
    for cur in range(1, n + 1):
        if dist[cur] == INF: continue
        for nxt, cost in edges[cur]:
            if dist[nxt] > dist[cur] + cost:
                return -1
    return '\n'.join(map(lambda x: str(x) if x != INF else '-1', dist[2:]))


def main():
    n, m = map(int, input().split())
    edges = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        edges[a].append((b, c))
    print(bellman_ford(n, edges))


if __name__ == "__main__":
    main()
