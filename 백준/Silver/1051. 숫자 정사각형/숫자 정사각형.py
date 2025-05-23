import sys
input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    nums = [list(map(int, list(input().rstrip()))) for _ in range(n)]
    for l in range(min(n,m)-1, 0, -1):
        for i in range(n-l):
            for j in range(m-l):
                if nums[i][j] == nums[i][j+l] and nums[i][j] == nums[i+l][j] and nums[i][j] == nums[i+l][j+l]:
                    print((l+1)**2)
                    return
    print(1)

if __name__ == "__main__":
    main()