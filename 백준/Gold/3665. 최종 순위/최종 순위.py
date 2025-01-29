import sys
from collections import deque
input = sys.stdin.readline

def solve(n, r_rank, h_rank):
    ans = []
    queue = deque()
    for i in range(1, n+1):
        if h_rank[i] == 0:
            queue.append(i)
    while queue:
        if len(queue) > 1:
            return "?"
        cur = queue.popleft()
        h_rank[cur] -= 1
        ans.append(cur)
        for i in range(1, n+1):
            if r_rank[cur][i] == 1:
                r_rank[cur][i] = 0
                h_rank[i] -= 1
        for i in range(1, n+1):
            if h_rank[i] == 0:
                queue.append(i)
    if len(ans) != n:
        return "IMPOSSIBLE"
    return " ".join(map(str, ans))


def case():
    n = int(input())
    ranking = list(map(int, input().split()))
    relative_ranking = [[0] * (n + 1) for _ in range(n + 1)]
    higher_ranker = [0] * (n + 1)
    for i in range(n - 1):
        for j in range(i + 1, n):
            relative_ranking[ranking[i]][ranking[j]] = 1
            higher_ranker[ranking[j]] += 1
    m = int(input())
    for _ in range(m):
        a, b = map(int, input().split())
        if relative_ranking[a][b] == 1:
            relative_ranking[a][b] = 0
            higher_ranker[a] += 1
            relative_ranking[b][a] = 1
            higher_ranker[b] -= 1
        else:
            relative_ranking[a][b] = 1
            higher_ranker[b] += 1
            relative_ranking[b][a] = 0
            higher_ranker[a] -= 1
    print(solve(n, relative_ranking, higher_ranker))

def main():
    T = int(input())
    for _ in range(T):
        case()

if __name__ == "__main__":
    main()