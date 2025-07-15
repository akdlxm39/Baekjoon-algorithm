import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def diameter_of_tree(n, tree, cur, ans):
    tmp = []
    for child, weight in tree[cur]:
        tmp.append(diameter_of_tree(n, tree, child, ans) + weight)
    if not tmp:
        return 0
    if len(tmp) > 1:
        tmp.sort(reverse=True)
        ans[0] = max(ans[0], tmp[0] + tmp[1])
    return tmp[0]

def main():
    n = int(input())
    tree = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        parent, child, weight = map(int, input().split())
        tree[parent].append((child, weight))
    ans = [0]
    tmp = diameter_of_tree(n, tree, 1, ans)
    print(max(tmp, ans[0]))

if __name__ == "__main__":
    main()