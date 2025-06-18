import sys
input = sys.stdin.readline

def check(n, h, ladder):
    for i in range(1, n):
        cur = i
        for j in range(1, h+1):
            cur = ladder[j][cur]
        if cur != i:
            return False
    return True

def bruteforce(n, h, ladder, cross_cnt, x, y, ans):
    if cross_cnt == 3 or x == n:
        if check(n, h, ladder) and ans[0] > cross_cnt:
            ans[0] = cross_cnt
        return
    if y == h:
        nxt_x, nxt_y = x + 1, 1
    else:
        nxt_x, nxt_y = x, y + 1
    bruteforce(n, h, ladder, cross_cnt, nxt_x, nxt_y, ans)
    if ladder[y][x]==x and ladder[y][x+1] == x+1 and cross_cnt+1<ans[0]:
        ladder[y][x], ladder[y][x+1] = x+1, x
        bruteforce(n, h, ladder, cross_cnt+1, nxt_x, nxt_y, ans)
        ladder[y][x], ladder[y][x+1] = x, x+1


def main():
    n, m, h = map(int, input().split())
    ladder = [list(range(n+1)) for _ in range(h+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        ladder[a][b] = b+1
        ladder[a][b+1] = b
    ans = [4]
    bruteforce(n, h, ladder, 0, 1, 1, ans)
    print(ans[0] if ans[0]<4 else -1)

if __name__ == "__main__":
    main()