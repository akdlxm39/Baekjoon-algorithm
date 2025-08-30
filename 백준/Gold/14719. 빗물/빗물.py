import sys

input = sys.stdin.readline


def main():
    h, w = map(int, input().split())
    buildings = list(map(int, input().split()))
    stack = []
    ans = 0
    for i in range(w):
        while len(stack) > 1 and buildings[stack[-1]] <= buildings[i]:
            h_gap = min(buildings[stack[-2]], buildings[i]) - buildings[stack[-1]]
            w_gap = i - stack[-2] - 1
            ans += h_gap * w_gap
            stack.pop()
        if len(stack) == 1 and buildings[stack[-1]] <= buildings[i]:
            stack.pop()
        stack.append(i)
    print(ans)


if __name__ == "__main__":
    main()
