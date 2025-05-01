import sys
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        stickers = zip(map(int, input().split()), map(int, input().split()))
        top = bottom = non = 0
        for t, b in stickers:
            top, bottom, non = (max(bottom, non) + t,
                                max(top, non) + b,
                                max(top, bottom))
        print(max(top, bottom, non))

if __name__ == "__main__":
    main()