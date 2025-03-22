import sys
input = sys.stdin.readline

def lower_bound(arr, x):
    l, r = 0, len(arr)
    while l < r:
        m = (l+r)//2
        if arr[m] > x:
            l = m + 1
        else:
            r = m
    return l

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    dp = [10000001]
    for x in arr:
        if x < dp[-1]:
            dp.append(x)
            cnt += 1
        else:
            dp[lower_bound(dp, x)] = x
    print(n-cnt)


if __name__ == "__main__":
    main()