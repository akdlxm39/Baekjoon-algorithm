import sys
from heapq import heappush, heappushpop
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        small_nums = []
        big_nums = []
        ans = []
        for _ in range((n-1)//10+1):
            for num in map(int, input().split()):
                if len(small_nums) == len(big_nums):
                    heappush(big_nums, -heappushpop(small_nums, -num))
                    ans.append(big_nums[0])
                else:
                    heappush(small_nums, -heappushpop(big_nums, num))
        print(n//2+1)
        for i in range(0, n//2+1, 10):
            print(' '.join(map(str, ans[i:i+10])))

if __name__ == "__main__":
    main()