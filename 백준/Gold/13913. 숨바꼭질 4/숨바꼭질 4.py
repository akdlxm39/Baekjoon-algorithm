import sys
from collections import deque

input = sys.stdin.readline


def main():
    n, k = map(int, input().split())
    if n >= k:
        print(n - k)
        print(*range(n, k - 1, -1))
        return
    nxt = [-1] * (k * 2 + 1)
    queue = deque([k])
    while queue:
        cur = queue.popleft()
        if cur % 2 == 0:
            prev = cur // 2
            if nxt[prev] == -1:
                nxt[prev] = cur
                if prev == n: break
                queue.append(prev)
        if cur > 0:
            prev = cur - 1
            if nxt[prev] == -1:
                nxt[prev] = cur
                if prev == n: break
                queue.append(prev)
        if cur < k * 2:
            prev = cur + 1
            if nxt[prev] == -1:
                nxt[prev] = cur
                if prev == n: break
                queue.append(prev)
    ans = [n]
    while n != k:
        n = nxt[n]
        ans.append(n)
    print(len(ans) - 1)
    print(*ans)


if __name__ == "__main__":
    main()
