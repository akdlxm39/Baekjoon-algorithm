import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e6))

def dfs(adj_list, visited, cur, prev, idx, ans):
    visited[cur] = idx
    res = idx
    cnt = 0
    for nxt in adj_list[cur]:
        if nxt == prev: continue
        if visited[nxt] == 0:
            cnt += 1
            tmp, idx = dfs(adj_list, visited, nxt, cur, idx+1, ans)
            if prev and tmp>=visited[cur]: ans.add(cur)
            res = min(res, tmp)
        else:
            res = min(res, visited[nxt])
    if not prev and cnt >= 2:
        ans.add(cur)
    return res, idx

def main():
    v, e = map(int, input().split())
    adj_list = [set() for _ in range(v+1)]
    for _ in range(e):
        a, b = map(int, input().split())
        adj_list[a].add(b)
        adj_list[b].add(a)
    visited = [0] * (v+1)
    ans = set()
    for i in range(1, v+1):
        if not visited[i]:
            dfs(adj_list, visited, i, 0, 1, ans)
    print(len(ans))
    if len(ans) > 0:
        print(*sorted(ans))

if __name__ == "__main__":
    main()