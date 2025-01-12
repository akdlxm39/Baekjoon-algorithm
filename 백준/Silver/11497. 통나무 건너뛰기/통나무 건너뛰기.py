import sys
input = sys.stdin.readline

def main():
    T = int(input())
    for _ in range(T):
        n = int(input())
        l = sorted(list(map(int, input().split())))
        level = max(abs(a-b) for a, b in zip(l, l[2:]))
        print(level)

if __name__ == "__main__":
    main()