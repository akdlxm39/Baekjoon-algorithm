import sys
input = sys.stdin.readline

def main():
    f = float(input())
    f = f if f<=1 else 1
    ans = (f*f)/4
    print(ans)

if __name__ == "__main__":
    main()