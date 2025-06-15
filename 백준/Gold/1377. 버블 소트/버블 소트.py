import sys
input = sys.stdin.readline

def main():
    n = int(input())
    nums = sorted((int(input()), i) for i in range(n))
    ans = max(j-i for i, (_, j) in enumerate(nums))+1
    print(ans)

if __name__ == "__main__":
    main()