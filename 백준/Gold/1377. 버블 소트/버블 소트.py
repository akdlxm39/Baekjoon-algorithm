import sys
input = sys.stdin.readline

def main():
    n = int(input())
    nums = [int(input()) for _ in range(n)]
    sort_idx = sorted(range(n), key=lambda i: nums[i])
    ans = max(j-i for i, j in enumerate(sort_idx))+1
    print(ans)

if __name__ == "__main__":
    main()