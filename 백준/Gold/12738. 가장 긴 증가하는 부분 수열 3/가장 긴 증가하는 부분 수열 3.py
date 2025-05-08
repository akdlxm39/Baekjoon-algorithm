import sys
from bisect import bisect_left
input = sys.stdin.readline

def main():
    n = int(input())
    x, *nums = map(int, input().split())
    ans_list = [x]
    for a in nums:
        if ans_list[-1] < a:
            ans_list.append(a)
        else:
            ans_list[bisect_left(ans_list, a)] = a
    print(len(ans_list))

if __name__ == "__main__":
    main()