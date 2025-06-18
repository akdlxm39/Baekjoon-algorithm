import sys
input = sys.stdin.readline

def check(n, h, ladder):
    for i in range(n-1):
        cur = i
        for j in range(h):
            cur = ladder[j][cur]
        if cur != i:
            return False
    return True

def bruteforce(n, h, ladder, cross_cnt, cur):
    if cross_cnt == 0:
        return check(n, h, ladder)
    for nxt in range(cur, (n-1)*h):
        x, y = nxt//h, nxt%h
        if ladder[y][x]==x and ladder[y][x+1]==x+1:
            ladder[y][x], ladder[y][x+1] = x+1, x
            if bruteforce(n, h, ladder, cross_cnt-1, nxt+1):
                return True
            ladder[y][x], ladder[y][x+1] = x, x+1
    return False

def main():
    n, m, h = map(int, input().split())
    ladder = [list(range(n)) for _ in range(h)]
    for _ in range(m):
        a, b = map(int, input().split())
        ladder[a-1][b-1] = b
        ladder[a-1][b] = b-1
    for i in range(4):
        if bruteforce(n, h, ladder, i, 0):
            print(i)
            break
    else:
        print(-1)

if __name__ == "__main__":
    main()