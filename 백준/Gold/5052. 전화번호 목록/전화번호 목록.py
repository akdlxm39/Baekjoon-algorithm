import sys
input = sys.stdin.readline

def main():
    for _ in range(int(input())):
        n = int(input())
        nums = sorted(input().rstrip() for _ in range(n))
        for i in range(1, n):
            x = min(len(nums[i-1]), len(nums[i]))
            for j in range(x):
                if nums[i][j] != nums[i-1][j]:
                    break
            else:
                break
        else:
            print("YES")
            continue
        print("NO")

if __name__ == "__main__":
    main()