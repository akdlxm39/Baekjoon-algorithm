import sys
from collections import deque
input = sys.stdin.readline

def adj_dist(room, pos, pos_dict, i, adj):
    w, h = len(room[0]), len(room)
    visited = [[False]*w for _ in range(h)]
    queue = deque([(pos[i], 0)])
    visited[pos[i][0]][pos[i][1]] = True
    cnt = 0
    while queue:
        (x, y), dist = queue.popleft()
        for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
            nx, ny = x+dx, y+dy
            if not (0<=nx<h and 0<=ny<w) or visited[nx][ny] or room[nx][ny]=='x':
                continue
            if room[nx][ny] == '*':
                j = pos_dict[(nx, ny)]
                adj[i][j] = adj[j][i] = dist+1
                cnt += 1
            visited[nx][ny] = True
            queue.append(((nx, ny), dist+1))
    return i!=0 or cnt == len(pos)-1

def position(room):
    w, h = len(room[0]), len(room)
    pos = []
    start_pos = (0, 0)
    for i in range(h):
        for j in range(w):
            if room[i][j] == '.' or room[i][j] == 'x':
                pass
            elif room[i][j] == '*':
                pos.append((i, j))
            else:
                start_pos = (i, j)
    return [start_pos] + pos

def dfs(n, adj, visited, cur, cnt, res, ans):
    if res > ans[0]:
        return
    if cnt == n-1:
        ans[0] = res
        return
    visited[cur] = True
    for nxt, dist in enumerate(adj[cur]):
        if not visited[nxt]:
            dfs(n, adj, visited, nxt, cnt+1, res+dist, ans)
    visited[cur] = False
    return

def main():
    while True:
        w, h = map(int, input().split())
        if w==0 and h==0:
            break
        room = [list(input().rstrip()) for _ in range(h)]
        pos = position(room)
        pos_dict = {x:i for i, x in enumerate(pos)}
        n = len(pos)
        adj = [[-1]*n for _ in range(n)]
        for i in range(n-1):
            if not adj_dist(room, pos, pos_dict, i, adj):
                print(-1)
                break
            room[pos[i][0]][pos[i][1]] = '.'
            adj[i][i] = adj[i][0] = 0
        else:
            adj[n-1][n-1] = adj[n-1][0] = 0
            visited = [False]*n
            ans = [10000000]
            dfs(n, adj, visited, 0, 0, 0, ans)
            print(ans[0])

if __name__ == "__main__":
    main()