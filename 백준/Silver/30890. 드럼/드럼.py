import sys
input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    x = n * m
    ans = [0]*x
    for i in range(n-1, x, n):
        ans[i] += 2
    for i in range(m-1, x, m):
        ans[i] += 1
    print(''.join(map(str, filter(lambda x: x, ans))))

if __name__ == "__main__":
    main()