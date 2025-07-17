import sys
input = sys.stdin.readline

def assign(can_work, who_work, visited, who):
    for work in can_work[who]:
        if who_work[work] == 0:
            who_work[work] = who
            return True
    for work in can_work[who]:
        if visited[work]: continue
        visited[work] = True
        if who_work[work] == who: continue
        if assign(can_work, who_work, visited, who_work[work]):
            who_work[work] = who
            return True
    return False

def main():
    n, m = map(int, input().split())
    can_work = [[]] + [list(map(int, input().split()))[1:] for _ in range(n)]
    who_work = [0] * (m + 1)
    ans = 0
    for i in range(1, n + 1):
        visited = [False] * (m + 1)
        ans += assign(can_work, who_work, visited, i)
        ans += assign(can_work, who_work, visited, i)
        if ans == m:
            break
    print(ans)

if __name__ == "__main__":
    main()