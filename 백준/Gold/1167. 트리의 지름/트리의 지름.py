import sys

sys.setrecursionlimit(100007)
input = sys.stdin.readline

def get_diameter(tree, visited, cur):
    visited[cur] = True
    children = []
    answers = []
    for nxt, weight in tree[cur]:
        if visited[nxt]:
            continue
        c, a = get_diameter(tree, visited, nxt)
        children.append(c + weight)
        answers.append(a)
    children_cnt = len(children)
    if children_cnt == 0:
        return 0, 0
    elif children_cnt == 1:
        return children[0], answers[0]
    else:
        children.sort(reverse=True)
        return children[0], max(max(answers), children[0] + children[1])


def main():
    n = int(input())
    tree = [[] for _ in range(n + 1)]
    for _ in range(n):
        line = tuple(map(int, input().split()))
        for j in range(1, len(line) - 1, 2):
            tree[line[0]].append((line[j], line[j + 1]))
    visited = [False] * (n + 1)
    print(max(get_diameter(tree, visited, 1)))


if __name__ == "__main__":
    main()
