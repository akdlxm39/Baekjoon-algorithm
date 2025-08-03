import sys

sys.setrecursionlimit(100000)
input = sys.stdin.readline


def dfs(n, needToTrue, visited, finished, stack, cur, idx):
    stack.append(cur)
    res = visited[cur] = idx
    for nxt in needToTrue[cur]:
        if not visited[nxt]:
            tmp, idx = dfs(n, needToTrue, visited, finished, stack, nxt, idx + 1)
            res = min(res, tmp)
        elif not finished[nxt]:
            res = min(res, visited[nxt])
    if res == visited[cur]:
        while stack:
            top = stack.pop()
            finished[top] = res
            if cur == top:
                break
    return res, idx


def main():
    n, m = map(int, input().split())

    needToTrue = [[] for _ in range(2 * n + 1)]
    for i in range(1, m + 1):
        a, b = map(int, input().split())
        needToTrue[-a].append(b)
        needToTrue[-b].append(a)
    visited = [1] + [0] * (2 * n)
    finished = [1] + [0] * (2 * n)
    idx = 0
    stack = []
    for i in range(-n, n + 1):
        if visited[i]: continue
        _, idx = dfs(i, needToTrue, visited, finished, stack, i, idx + 1)
    for i in range(1, n + 1):
        if finished[i] == finished[-i]:
            print(0)
            break
    else:
        print(1)


if __name__ == "__main__":
    main()
