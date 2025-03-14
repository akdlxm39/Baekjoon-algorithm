import sys
input = sys.stdin.readline

def main():
    f = float(input())
    ans = (min(1, f**2))/4
    print(ans)

if __name__ == "__main__":
    main()