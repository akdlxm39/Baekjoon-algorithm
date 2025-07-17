import sys
input = sys.stdin.readline

def assign(can_work, who_work, visited, who):
    for work in can_work[who]:
        if visited[work]: continue
        visited[work] = True
        if who_work[work] == who: continue
        if who_work[work] == 0 or assign(can_work, who_work, visited, who_work[work]):
            who_work[work] = who
            return True
    return False

def main():
    n, m = map(int, input().split())
    can_work = [[] for _ in range(n + 1)]
    who_work = [0] * (m + 1)
    for i in range(1, n + 1):
        _, *works = list(map(int, input().split()))
        if works:
            can_work[i] = works
    ans = 0
    for i in range(1, n + 1):
        ans += assign(can_work, who_work, [False] * (m + 1), i)
        ans += assign(can_work, who_work, [False] * (m + 1), i)
    print(ans)

if __name__ == "__main__":
    main()