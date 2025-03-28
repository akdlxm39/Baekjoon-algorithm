import sys
input = sys.stdin.readline

def main():
    n = int(input())
    dp = 0
    tmp = 1
    for i in range(n-1):
        dp = (dp*2+tmp)%1_000_000_007
        tmp = -tmp
    print(dp)

if __name__ == "__main__":
    main()