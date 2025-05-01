import sys
from collections import deque
input = sys.stdin.readline

def bfs(adj_matrix, adj_list):
    for i, line in enumerate(adj_list):
        queue = deque(line)
        while queue:
            cur = queue.popleft()
            for nxt in adj_list[cur]:
                if not adj_matrix[i][nxt]:
                    adj_matrix[i][nxt] = 1
                    queue.append(nxt)

def main():
    n = int(input())
    adj_matrix = [list(map(int, input().split())) for _ in range(n)]
    adj_list = []
    for line in adj_matrix:
        adj_list.append([i for i, x in enumerate(line) if x])
    bfs(adj_matrix, adj_list)
    print('\n'.join(' '.join(map(str, line)) for line in adj_matrix))

if __name__ == "__main__":
    main()