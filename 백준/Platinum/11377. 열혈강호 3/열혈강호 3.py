import sys

input = sys.stdin.readline


def assign(can_work, assigned, visited, cur):
    for work in can_work[cur]:
        if assigned[work] == -1:
            assigned[work] = cur
            return True
            
    for work in can_work[cur]:
        if visited[work]: continue
        visited[work] = True
        if  assign(can_work, assigned, visited, assigned[work]):
            assigned[work] = cur
            visited[work] = False
            return True
    return False


def main():
    n, m, k = map(int, input().split())
    can_work = [[] for _ in range(n + 1)]
    for i in range(1, n + 1):
        cnt, *works = map(int, input().split())
        if cnt:
            can_work[i] += works
    assigned = [-1] * (m + 1)
    ans = 0
    visited = [False] * (m + 1)
    for i in range(1, n + 1):
        if assign(can_work, assigned, visited, i):
            ans += 1
    for i in range(1, n + 1):
        if assign(can_work, assigned, visited, i):
            ans += 1
            k -= 1
            if not k:
                break
    print(ans)


if __name__ == "__main__":
    main()
