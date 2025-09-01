import sys

input = sys.stdin.readline


def main():
    h, w = map(int, input().split())
    buildings = list(map(int, input().split()))
    left_max = [0] * w
    right_max = [0] * w
    left_max[0] = buildings[0]
    right_max[-1] = buildings[-1]
    for i in range(1, w):
        left_max[i] = max(left_max[i - 1], buildings[i])
    for i in range(w - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], buildings[i])
    ans = 0
    for i in range(w):
        ans += min(left_max[i], right_max[i]) - buildings[i]
    print(ans)


if __name__ == "__main__":
    main()
