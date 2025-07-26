import sys

input = sys.stdin.readline
sys.setrecursionlimit(int(1e7))


def dfs(adj_list, visited, cur, prev, idx, ans):
    visited[cur] = idx
    res = idx
    for nxt in adj_list[cur]:
        if nxt == prev: continue
        if visited[nxt] == 0:
            tmp, idx = dfs(adj_list, visited, nxt, cur, idx + 1, ans)
            if visited[cur] < tmp:
                ans.add((cur, nxt) if cur < nxt else (nxt, cur))
            else:
                res = min(res, tmp)
        else:
            res = min(res, visited[nxt])

    return res, idx


def main():
    v, e = map(int, input().split())
    adj_list = [[] for _ in range(v + 1)]
    for _ in range(e):
        a, b = map(int, input().split())
        adj_list[a].append(b)
        adj_list[b].append(a)
    visited = [0] * (v + 1)
    ans = set()
    dfs(adj_list, visited, 1, 0, 1, ans)
    print(len(ans))
    if len(ans):
        print('\n'.join(map(lambda x: ' '.join(map(str, x)), sorted(ans))))


if __name__ == "__main__":
    main()
