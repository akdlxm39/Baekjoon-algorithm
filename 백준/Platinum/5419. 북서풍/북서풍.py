import sys
from bisect import bisect_right

input = sys.stdin.readline


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        islands = [tuple(map(int, input().split())) for _ in range(n)]
        islands.sort(key=lambda a: (a[0], -a[1]))
        prevs = [-islands[0][1]]
        ans = 0
        for i in range(1, n):
            pivot = bisect_right(prevs, -islands[i][1])
            ans += pivot
            prevs.insert(pivot, -islands[i][1])
        print(ans)


if __name__ == "__main__":
    main()
