import sys
from collections import deque
input = sys.stdin.readline

def make_tree(n, adj_list, parents, depths):
    queue = deque([1])
    depths[1] = 0
    while queue:
        cur = queue.popleft()
        for nxt, cost in adj_list[cur]:
            if depths[nxt] == -1:
                depths[nxt] = depths[cur] + 1
                parents[0][0][nxt] = cur
                parents[1][0][nxt] = parents[2][0][nxt] = cost
                queue.append(nxt)
    for j in range(17):
        for i in range(1, n+1):
            parents[0][j+1][i] = parents[0][j][parents[0][j][i]]
            if parents[0][j+1][i] == 0: continue
            parents[1][j+1][i] = min(parents[1][j][i], parents[1][j][parents[0][j][i]])
            parents[2][j+1][i] = max(parents[2][j][i], parents[2][j][parents[0][j][i]])
    return

def main():
    n = int(input())
    adj_list = [[] for _ in range(n+1)]
    for _ in range(n-1):
        u, v, w = map(int, input().split())
        adj_list[u].append((v, w))
        adj_list[v].append((u, w))
    depths = [-1] * (n+1)
    parents = [[[0] * (n+1) for _ in range(18)] for _ in range(3)]
    make_tree(n, adj_list, parents, depths)

    m = int(input())
    answers = [''] * m
    for i in range(m):
        a, b = map(int, input().split())
        min_ans, max_ans = 1_000_001, 0
        if depths[a] < depths[b]:
            a, b = b, a
        while depths[a] != depths[b]:
            tmp = len(bin(depths[a] - depths[b])) - 3
            min_ans = min(min_ans, parents[1][tmp][a])
            max_ans = max(max_ans, parents[2][tmp][a])
            a = parents[0][tmp][a]
        while a != b:
            tmp = len(bin(depths[a])) - 2
            while tmp > 0 and parents[0][tmp][a] == parents[0][tmp][b]:
                tmp -= 1
            min_ans = min(min_ans, parents[1][tmp][a], parents[1][tmp][b])
            max_ans = max(max_ans, parents[2][tmp][a], parents[2][tmp][b])
            a, b = parents[0][tmp][a], parents[0][tmp][b]
        answers[i] = str(min_ans)+' '+str(max_ans)
    print('\n'.join(answers))

if __name__ == "__main__":
    main()