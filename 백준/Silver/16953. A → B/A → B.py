import sys
from collections import deque
input = sys.stdin.readline

def main():
    a, b = map(int, input().split())
    cnt = 1
    while a < b:
        if b % 2 == 0:
             b //= 2
        elif b % 10 == 1:
            b //= 10
        else:
            print(-1)
            break
        cnt += 1
    else:
        print(cnt if a == b else -1)

if __name__ == "__main__":
    main()