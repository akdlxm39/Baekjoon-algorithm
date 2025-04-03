import sys
input = sys.stdin.readline

def main():
    n = int(input())
    amenities = set(tuple(map(int, input().split())) for _ in range(n))
    length_min = 1000000000000
    ans = amenities.pop()
    amenities.add(ans)
    for ax, ay in amenities:
        length_max = 0
        for bx, by in amenities:
            if ax!=bx or ay!=by:
                length_max = max(length_max, (bx-ax)**2+(by-ay)**2)
        if length_max < length_min:
            length_min = length_max
            ans = (ax, ay)
    print(*ans)

if __name__ == "__main__":
    main()