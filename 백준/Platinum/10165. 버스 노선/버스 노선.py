import sys
input = sys.stdin.readline

def main():
    n, m = int(input()), int(input())
    lines = dict()
    passing_zero = set()
    for i in range(1, m+1):
        a, b = map(int, input().split())
        dist = b - a + n*(a>b)
        if lines.get(a, (0, 0))[0] < dist:
            lines[a] = (dist, i)
            if 0<b<a:
                passing_zero.add(a)
    passing_zero = [(x, lines[x]) for x in passing_zero]
    arr = sorted(passing_zero) + sorted(lines.items())
    cur = arr[0]
    ans = {cur[1][1]}
    for x in arr[1:]:
        if cur[1][0] - (x[0]- cur[0]+n)%n >= x[1][0]:
            continue
        else:
            ans.add(x[1][1])
            cur = x
    print(*sorted(ans))



if __name__ == "__main__":
    main()