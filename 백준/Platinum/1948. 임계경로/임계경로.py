import sys
from collections import deque
input = sys.stdin.readline

def main():
    n, m = int(input()), int(input())
    roads = [{} for _ in range(n+1)]
    degree = [0] * (n + 1)
    for _ in range(m):
        a, b, c = map(int, input().split())
        roads[a][b] = max(roads[a].get(b, 0), c)
        degree[b] += 1
    s, d = map(int, input().split())
    prevs = [[0] for _ in range(n + 1)]
    queue = deque([s])
    while queue:
        cur = queue.popleft()
        for nxt, nxt_time in roads[cur].items():
            nxt_time += prevs[cur][0]
            if prevs[nxt][0] < nxt_time:
                prevs[nxt] = [nxt_time, cur]
            elif prevs[nxt][0] == nxt_time:
                prevs[nxt].append(cur)
            degree[nxt] -= 1
            if degree[nxt] == 0:
                queue.append(nxt)
    print(prevs[d][0])
    ans = 0
    queue = deque([d])
    visited = [False] * (n + 1)
    while queue:
        cur = queue.popleft()
        for prev in prevs[cur][1:]:
            ans += 1
            if visited[prev]: continue
            visited[prev] = True
            queue.append(prev)

    print(ans)



if __name__ == "__main__":
    main()