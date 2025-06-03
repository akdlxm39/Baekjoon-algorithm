import sys
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        candidates = sorted(tuple(map(int, input().split())) for _ in range(n))
        high = candidates[0][1]
        ans = 1
        for _, x in candidates[1:]:
            if x < high:
                ans += 1
                high = x
        print(ans)

if __name__ == "__main__":
    main()