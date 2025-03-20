import sys
input = sys.stdin.readline

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    enum = [(x, i) for i, x in enumerate(arr)]
    enum.sort()
    ans = [0] * n
    for i, (_, x) in enumerate(enum):
        ans[x] = i
    print(*ans)

if __name__ == "__main__":
    main()