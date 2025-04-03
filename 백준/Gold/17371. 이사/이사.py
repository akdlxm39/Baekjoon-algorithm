import sys
input = sys.stdin.readline

def main():
    n = int(input())
    amenities = [tuple(map(int, input().split())) for _ in range(n)]
    length_min = 1000000000000
    ans = amenities[0]
    for i in range(n):
        length_max = 0
        tmp = amenities[i]
        for j in range(n):
            if i == j:
                continue
            length = (amenities[j][0]-amenities[i][0])**2 + (amenities[j][1]-amenities[i][1])**2
            if length > length_max:
                length_max = length
        if length_max < length_min:
            length_min = length_max
            ans = tmp
    print(*ans)

if __name__ == "__main__":
    main()