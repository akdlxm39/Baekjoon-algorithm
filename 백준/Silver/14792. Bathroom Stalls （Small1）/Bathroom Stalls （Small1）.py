import sys
from math import log
input = sys.stdin.readline

def main():
    T = int(input())
    for i in range(1, T + 1):
        n, k = map(int, input().split())
        ans = (n-k)/(2**int(log(k, 2) + 1))
        print(f"Case #{i}: {int(ans+0.5)} {int(ans)}")

if __name__ == "__main__":
    main()