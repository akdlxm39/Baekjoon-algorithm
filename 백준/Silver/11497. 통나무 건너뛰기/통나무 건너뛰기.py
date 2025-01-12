import sys
input = sys.stdin.readline

def main():
    T = int(input())
    for _ in range(T):
        n = int(input())
        l = sorted(list(map(int, input().split())))
        ans = l[::2] + l[1::2][::-1] + [l[0]]
        max_gap = max(abs(a-b) for a, b in zip(ans, ans[1:]))
        print(max_gap)

if __name__ == "__main__":
    main()