import sys
input = sys.stdin.readline

def main():
    n = int(input())
    ans = list(input().rstrip())
    for _ in range(n-1):
        for i, c in enumerate(input().rstrip()):
            if ans[i] != c:
                ans[i] = '?'
    print(''.join(ans))

if __name__ == "__main__":
    main()