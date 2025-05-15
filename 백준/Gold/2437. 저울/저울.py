import sys
input = sys.stdin.readline

def main():
    n = int(input())
    weights = sorted(map(int, input().split()))
    ans = 1
    for w in weights:
        if ans < w:
            break
        ans += w
    print(ans)

if __name__ == "__main__":
    main()