import sys
from collections import deque
input = sys.stdin.readline

def main():
    n = int(input())
    parents = list(map(int, input().split()))
    child = [[] for _ in range(n)]
    root = 0
    for i in range(n):
        if parents[i] == -1:
            root = i
        else:
            child[parents[i]].append(i)
    delete = int(input())
    queue = deque([root])
    ans = 0
    while queue:
        cur = queue.popleft()
        if cur == delete:
            continue
        if child[cur]:
            if child[cur] == [delete]:
                ans += 1
                continue
            for nxt in child[cur]:
                queue.append(nxt)
        else:
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()