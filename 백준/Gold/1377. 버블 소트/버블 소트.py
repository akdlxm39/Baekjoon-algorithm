import sys
input = sys.stdin.readline

def main():
    n = int(input())
    nums = [int(input()) for _ in range(n)]
    idx = sorted(range(n), key=lambda i: nums[i])
    ans = max(i-j for j, i in enumerate(idx))+1
    print(ans)

if __name__ == "__main__":
    main()