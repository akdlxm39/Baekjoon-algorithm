import sys
from bisect import bisect_left
input = sys.stdin.readline

def main():
    l = int(input())
    s = [0] + sorted(map(int, input().split()))
    n = int(input())
    i = bisect_left(s, n)
    if s[i] == n:
        print(0)
    else:
        left, right = s[i-1], s[i]
        print((n-left)*(right-n)-1)

if __name__ == "__main__":
    main()