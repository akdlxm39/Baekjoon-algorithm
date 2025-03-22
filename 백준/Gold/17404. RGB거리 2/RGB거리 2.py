import sys
input = sys.stdin.readline

def main():
    N = int(input())
    rr, gg, bb = map(int, input().split())
    rg, rb, gr, gb, br, bg = (10000,) * 6
    for i in range(1, N):
        r, g, b = map(int, input().split())
        rr, rg, rb = min(rg, rb) + r, min(rr, rb) + g, min(rr, rg) + b
        gr, gg, gb = min(gg, gb) + r, min(gr, gb) + g, min(gr, gg) + b
        br, bg, bb = min(bg, bb) + r, min(br, bb) + g, min(br, bg) + b
    print(min(rg, rb, gr, gb, br, bg))

if __name__ == "__main__":
    main()