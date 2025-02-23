import sys
input = sys.stdin.readline

def main():
    for _ in range(int(input())):
        n = int(input())
        nums = sorted(input().rstrip() for _ in range(n))
        for i in range(1, n):
            if nums[i].startswith(nums[i-1]):
                break
        else:
            print("YES")
            continue
        print("NO")

if __name__ == "__main__":
    main()