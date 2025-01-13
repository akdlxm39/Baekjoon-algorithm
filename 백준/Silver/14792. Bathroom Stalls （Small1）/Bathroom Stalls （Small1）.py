import sys
from heapq import heapify, heappush, heappop
from collections import deque
input = sys.stdin.readline

def main():
    gap = lambda x: (x // 2, (x - 1) // 2)
    T = int(input())
    for i in range(1, T + 1):
        n, k = map(int, input().split())
        dict = {n:1}
        q = deque([n])
        while q:
            cur = q.popleft()
            cnt = dict[cur]
            max_gap, min_gap = gap(cur)
            if k <= cnt:
                print(f"Case #{i}:", max_gap, min_gap)
                break
            k -= cnt
            if max_gap in q:
                dict[max_gap] += cnt
            else:
                dict[max_gap] = cnt
                q.append(max_gap)
            if min_gap in q:
                dict[min_gap] += cnt
            else:
                dict[min_gap] = cnt
                q.append(min_gap)

if __name__ == "__main__":
    main()