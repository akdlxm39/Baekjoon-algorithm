import sys
input = sys.stdin.readline

def main():
    n, a, b = map(int, input().split())
    ans = 0
    while a != b:
        a = (a+1)//2
        b = (b+1)//2
        ans += 1
    print(ans)

if __name__ == "__main__":
    main()