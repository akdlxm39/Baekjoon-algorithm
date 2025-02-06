import sys
from heapq import heapify, heappush, heappop
from itertools import product
input = sys.stdin.readline

def main():
    n = int(input())
    maps = [list(map(int, input().split())) for _ in range(n)]
    heap = []
    idx = 2
    for i, j in product(range(n), repeat=2):
        if maps[i][j] != 1:
            continue
        maps[i][j] = idx
        heappush(heap, (0, idx, i, j))
        while heap[0][0] == 0:
            _, cid, cx, cy = heappop(heap)
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            for dx, dy in directions:
                nx, ny = cx + dx, cy + dy
                if not (0 <= nx < n and 0 <= ny < n):
                    continue
                if maps[nx][ny] == 0:
                    maps[nx][ny] = cid
                    heappush(heap, (1, cid, nx, ny))
                elif maps[nx][ny] == 1:
                    maps[nx][ny] = cid
                    heappush(heap, (0, cid, nx, ny))
                elif maps[nx][ny] != cid:
                    print(1)
                    return
        idx += 1
    chk = 0
    ans = 0
    while heap:
        dist, cid, cx, cy = heappop(heap)
        if chk != cid:
            if ans:
                print(ans)
                break
            chk = cid
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if not (0 <= nx < n and 0 <= ny < n):
                continue
            if maps[nx][ny] == 0:
                maps[nx][ny] = cid
                heappush(heap, (dist + 1, cid, nx, ny))
            elif maps[nx][ny] < cid and ans == 0:
                ans = dist * 2 + 1
            elif maps[nx][ny] > cid:
                ans = dist * 2

if __name__ == "__main__":
    main()