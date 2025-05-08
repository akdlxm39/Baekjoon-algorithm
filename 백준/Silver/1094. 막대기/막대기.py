import sys
input = sys.stdin.readline

def main():
    x = int(input())
    ans = 0
    while x:
        ans += x&1
        x >>=1
    print(ans)

if __name__ == "__main__":
    main()