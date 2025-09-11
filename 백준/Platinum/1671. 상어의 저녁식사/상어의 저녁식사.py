import sys

input = sys.stdin.readline


def assign(can_eat, eaten, visited, cur):
    for nxt in can_eat[cur]:
        if eaten[nxt] == -1:
            eaten[nxt] = cur
            return True
    for nxt in can_eat[cur]:
        if visited[nxt]:
            continue
        visited[nxt] = True
        if assign(can_eat, eaten, visited, eaten[nxt]):
            eaten[nxt] = cur
            visited[nxt] = False
            return True
    return False


def main():
    n = int(input())
    sharks = [tuple(map(int, input().split())) for _ in range(n)]
    sharks.sort()
    can_eat = [[] for _ in range(n)]
    for i in range(n - 1):
        for j in range(i + 1, n):
            if sharks[i][0] <= sharks[j][0] and sharks[i][1] <= sharks[j][1] and sharks[i][2] <= sharks[j][2]:
                can_eat[j].append(i)
    eaten = [-1] * n
    visited = [False] * n
    ans = n
    for i in range(n):
        if assign(can_eat, eaten, visited, i):
            ans -= 1
        if assign(can_eat, eaten, visited, i):
            ans -= 1
    print(ans)


if __name__ == "__main__":
    main()
