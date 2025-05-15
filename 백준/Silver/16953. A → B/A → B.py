import sys
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
            b = 0
        cnt += 1
    print(cnt if a == b else -1)

if __name__ == "__main__":
    main()