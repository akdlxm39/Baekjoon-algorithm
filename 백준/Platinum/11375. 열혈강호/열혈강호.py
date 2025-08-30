import sys
sys.setrecursionlimit(int(1e5))
input = sys.stdin.readline

def assign(staff2work, assignment, visited, staff):
    for work in staff2work[staff]:
        if assignment[work] == -1:
            assignment[work] = staff
            return True
    for work in staff2work[staff]:
        if visited[work]: continue
        visited[work] = True
        if assign(staff2work, assignment, visited, assignment[work]):
            assignment[work] = staff
            return True
    return False

def main():
    n, m = map(int, input().split())
    staff2work = [[] for _ in range(n)]
    for i in range(n):
        _, *works = map(lambda x:int(x)-1, input().split())
        staff2work[i] = works
    assignment = [-1] * m
    ans = 0
    for staff in range(n):
        visited = [False] * m
        if assign(staff2work, assignment, visited, staff):
            ans += 1
    print(ans)

if __name__ == "__main__":
    main()