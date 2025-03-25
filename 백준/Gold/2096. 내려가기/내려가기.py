import sys
input = sys.stdin.readline

def main():
    n = int(input())
    dp_max = (0, 0, 0)
    dp_min = (0, 0, 0)
    for _ in range(n):
        a, b, c = map(int, input().split())
        dp_max = (a+max(dp_max[:2]), b+max(dp_max), c+max(dp_max[1:]))
        dp_min = (a+min(dp_min[:2]), b+min(dp_min), c+min(dp_min[1:]))
    print(max(dp_max), min(dp_min))

if __name__ == "__main__":
    main()