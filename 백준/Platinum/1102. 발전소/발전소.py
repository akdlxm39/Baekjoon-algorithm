import sys
from collections import deque
input = sys.stdin.readline
INF = int(1e9)

def main():
    n = int(input())
    costs = [list(map(int, input().split())) for _ in range(n)]
    on = input().rstrip()
    p = int(input())
    start_mask = 0
    for i in range(n):
        if on[i] == 'Y':
            start_mask += 1<<i
    dp = [INF] * (2**n)
    queue = deque([(0, start_mask)])
    ans = INF
    while queue:
        cur_cost, cur_mask = queue.popleft()
        if cur_cost > dp[cur_mask]: continue
        cur_on, cur_off = [], []
        for i in range(n):
            if cur_mask & 1<<i:
                cur_on.append(i)
            else:
                cur_off.append(i)
        if len(cur_on) >= p:
            ans = min(ans, cur_cost)
            continue
        for j in cur_off:
            nxt_mask = cur_mask | 1<<j
            for i in cur_on:
                nxt_cost = cur_cost + costs[i][j]
                if nxt_cost >= dp[nxt_mask]: continue
                dp[nxt_mask] = nxt_cost
                queue.append((nxt_cost, nxt_mask))
    print(ans if ans != INF else -1)

if __name__ == "__main__":
    main()