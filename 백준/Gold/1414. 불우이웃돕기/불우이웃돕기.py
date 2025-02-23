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
    lans = [[] for _ in range(n)]
    for i in range(n):
        s = input().rstrip()
        for j, c in enumerate(s):
            if c == '0':
                continue
            m = change(c)
            ans += m
            lans[i].append((m, j))
            lans[j].append((m, i))
    heap = []
    for x in lans[0]:
        heappush(heap, x)
    visited = [False] * n
    visited[0] = True
    cnt = n-1
    while heap and cnt:
        lan, cur = heappop(heap)
        if visited[cur]:
            continue
        ans -= lan
        visited[cur] = True
        cnt -= 1
        for x in lans[cur]:
            if visited[x[1]]:
                continue
            heappush(heap, x)
    print(-1 if cnt else ans)

if __name__ == "__main__":
    main()