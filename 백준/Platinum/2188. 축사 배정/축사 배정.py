import sys
input = sys.stdin.readline

def assign(cows, barns, visited, cur):
    for want in cows[cur]:
        if visited[want]: continue
        visited[want] = True
        if barns[want] == -1 or assign(cows, barns, visited, barns[want]):
            barns[want] = cur
            return True
    return False

def main():
    n, m = map(int, input().split())
    cows = [list(map(lambda x:int(x)-1, input().split()))[1:] for _ in range(n)]
    barns = [-1]*m
    ans = 0
    for i in range(n):
        visited = [False]*m
        if assign(cows, barns, visited, i):
            ans += 1
    print(ans)

if __name__ == "__main__":
    main()