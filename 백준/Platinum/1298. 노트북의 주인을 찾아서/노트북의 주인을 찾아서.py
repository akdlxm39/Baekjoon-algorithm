import sys

input = sys.stdin.readline


def try_matching(opinion, matching, visited, cur):
    for tmp in opinion[cur]:
        if visited[tmp]: continue
        visited[tmp] = True
        if not matching[tmp] or try_matching(opinion, matching, visited, matching[tmp]):
            matching[tmp] = cur
            return True
    return False


def main():
    n, m = map(int, input().split())
    opinion = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        opinion[a].append(b)
    matching = [0] * (n + 1)
    ans = 0
    for i in range(1, n + 1):
        visited = [False] * (n + 1)
        if try_matching(opinion, matching, visited, i):
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()
