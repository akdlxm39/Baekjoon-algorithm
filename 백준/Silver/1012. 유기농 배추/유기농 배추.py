import sys
input = sys.stdin.readline
dxdy = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def bfs(cabbages):
    count = 0
    while cabbages:
        queue = [cabbages.pop()]
        while queue:
            nxt_queue = []
            for cx, cy in queue:
                for dx, dy in dxdy:
                    nx, ny = cx + dx, cy + dy
                    if (nx, ny) in cabbages:
                        cabbages.remove((nx, ny))
                        nxt_queue.append((nx, ny))
            queue = nxt_queue
        count += 1
    return count

def main():
    t = int(input())
    for _ in range(t):
        m, n, k = map(int, input().split())
        cabbages = set(tuple(map(int, input().split())) for _ in range(k))
        print(bfs(cabbages))

if __name__ == "__main__":
    main()