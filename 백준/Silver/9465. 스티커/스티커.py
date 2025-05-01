import sys
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        stickers = [list(map(int, input().split())) for _ in range(2)]
        top, bottom, non = stickers[0][0], stickers[1][0], 0
        for i in range(1, n):
            top, bottom, non = (stickers[0][i] + max(bottom, non),
                                stickers[1][i] + max(top, non),
                                max(top, bottom))
        print(max(top, bottom, non))

if __name__ == "__main__":
    main()