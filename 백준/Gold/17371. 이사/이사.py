import sys
input = sys.stdin.readline

def main():
    n = int(input())
    amenities = set(tuple(map(int, input().split())) for _ in range(n))
    ans = (0, 0)
    length_min = 1000000000000
    for ax, ay in amenities:
        length_max = max((bx-ax)**2+(by-ay)**2 for bx, by in amenities)
        if length_max < length_min:
            length_min = length_max
            ans = (ax, ay)
    print(*ans)

if __name__ == "__main__":
    main()