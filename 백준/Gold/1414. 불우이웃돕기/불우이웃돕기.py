import sys
from heapq import heapify, heappush, heappop
input = sys.stdin.readline

def change(x):
    if 'a' <= x <= 'z':
        return ord(x)-96
    elif 'A' <= x <= 'Z':
        return ord(x)-38
    else:
        return 0

def main():
    n = int(input())
    ans = 0
    lans = [list(map(change, list(input().rstrip()))) for _ in range(n)]
    for l in lans:
        ans += sum(l)
    heap = []
    visited = [False] * n
    visited[0] = True
    for i in range(1, n):
        if lans[0][i]:
            heappush(heap, (lans[0][i], i))
        if lans[i][0]:
            heappush(heap, (lans[i][0], i))
    cnt = n-1
    while heap and cnt:
        lan, cur = heappop(heap)
        if visited[cur]:
            continue
        ans -= lan
        visited[cur] = True
        cnt -= 1
        for i in range(n):
            if visited[i]:
                continue
            if lans[cur][i]:
                heappush(heap, (lans[cur][i], i))
            if lans[i][cur]:
                heappush(heap, (lans[i][cur], i))
    print(-1 if cnt else ans)

if __name__ == "__main__":
    main()