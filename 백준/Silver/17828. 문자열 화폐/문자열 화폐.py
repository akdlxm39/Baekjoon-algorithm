import sys
input = sys.stdin.readline

def main():
    n, x = map(int, input().split())
    if n <= x <= n*26 :
        ans = ''
        while x <= (n-1)*26:
            ans += 'A'
            x -= 1
            n -= 1
        ans += chr(64 + x - (n-1)*26) + 'Z'*(n-1)
        print(ans)
    else:
        print('!')

if __name__ == "__main__":
    main()