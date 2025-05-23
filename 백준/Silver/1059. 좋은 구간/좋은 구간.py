import sys
from bisect import bisect_left
input = sys.stdin.readline

def main():
    l = int(input())
    s = [0] + sorted(map(int, input().split()))
    n = int(input())
    i = bisect_left(s, n)
    if s[i] == n:
        ans = 0
    else:
        left, right = s[i-1], s[i]
        ans = (n-left)*(right-n)-1
    print(ans)

if __name__ == "__main__":
    main()