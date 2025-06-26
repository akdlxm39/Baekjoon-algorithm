import sys
input = sys.stdin.readline

def main():
    n, m = int(input()), int(input())
    broken = set(input().split())
    ans = abs(100-n)
    for num in range(1000001):
        snum = str(num)
        for x in snum:
            if x in broken:
                break
        else:
            ans = min(ans, len(snum)+abs(num-n))
    print(ans)

if __name__ == "__main__":
    main()