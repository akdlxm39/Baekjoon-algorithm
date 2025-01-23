import sys
input = sys.stdin.readline

def Z(x, y, size, r, c):
    if size == 1:
        return 0
    half = size//2
    if x<=r<x+half and y<=c<y+half:
        return Z(x, y, half, r, c)
    elif x<=r<x+half and y+half<=c<y+size:
        return half*half + Z(x, y+half, half, r, c)
    elif x+half<=r<x+size and y<=c<y+half:
        return 2*half*half + Z(x+half, y, half, r, c)
    elif x+half<=r<x+size and y+half<=c<y+size:
        return 3*half*half + Z(x+half, y+half, half, r, c)

def main():
    n, r, c = map(int, input().split())
    print(Z(0, 0, 2**n, r, c))

if __name__ == "__main__":
    main()