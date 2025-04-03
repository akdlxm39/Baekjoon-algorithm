import sys
input = sys.stdin.readline

def main():
    n = int(input())
    amenities = [tuple(map(int, input().split())) for _ in range(n)]
    min_cmp = lambda a:max((x-a[0])**2+(y-a[1])**2 for x, y in amenities)
    ans = min(amenities, key=min_cmp)
    print(*ans)

if __name__ == "__main__":
    main()