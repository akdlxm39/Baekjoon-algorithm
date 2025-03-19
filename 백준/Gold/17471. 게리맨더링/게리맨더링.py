import sys
input = sys.stdin.readline

def check(adj, team):
    if not team:
        return False
    find = {list(team)[0]}
    adjs = set(adj[list(team)[0]])
    while adjs:
        cur = adjs.pop()
        if cur in find or cur not in team:
            continue
        find.add(cur)
        adjs |= set(adj[cur])
    return len(find) == len(team)

def makeTeam(n, populations, adj, team, cur, pop):
    if cur > n:
        if check(adj, team) and check(adj, (set(range(1, n+1))-team)):
            return abs(2*pop - sum(populations))
        return 100000
    res = 100000
    res = min(res, makeTeam(n, populations, adj, team|{cur}, cur + 1, pop + populations[cur]))
    res = min(res, makeTeam(n, populations, adj, team, cur+1, pop))
    return res

def main():
    n = int(input())
    populations = [0] + list(map(int, input().split()))
    adj = dict()
    for i in range(1, n+1):
        cnt, *x = map(int, input().split())
        adj[i] = x
    ans = makeTeam(n, populations, adj, {1}, 2, populations[1])
    print(ans if ans != 100000 else -1)

if __name__ == "__main__":
    main()