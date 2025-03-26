import sys
from collections import deque
input = sys.stdin.readline

def bfs(n, m, k, maps):
    size = n*m
    visited = [-1]*size
    queue = [0]
    visited[0] = k
    dist = 1
    while queue and visited[-1] == -1:
        nxt_queue = []
        for x in queue:
            nx = x+1
            if nx % m:
                nb = visited[x]-(maps[nx]=='1')
                if nb > visited[nx]:
                    visited[nx] = nb
                    nxt_queue.append(nx)
            nx = x-1
            if x % m:
                nb = visited[x]-(maps[nx]=='1')
                if nb > visited[nx]:
                    visited[nx] = nb
                    nxt_queue.append(nx)
            nx = x+m
            if nx < size:
                nb = visited[x]-(maps[nx]=='1')
                if nb > visited[nx]:
                    visited[nx] = nb
                    nxt_queue.append(nx)
            nx = x-m
            if nx >= 0:
                nb = visited[x]-(maps[nx]=='1')
                if nb > visited[nx]:
                    visited[nx] = nb
                    nxt_queue.append(nx)
        queue = nxt_queue
        dist += 1
    return dist if visited[-1] != -1 else -1

def main():
    n, m, k = map(int, input().split())
    maps = ''
    for _ in range(n):
        maps += input().rstrip()
    print(1 if n==1 and m==1 else bfs(n, m, k, maps))

if __name__ == "__main__":
    main()