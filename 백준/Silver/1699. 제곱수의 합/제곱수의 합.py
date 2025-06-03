import sys
input = sys.stdin.readline

def main():
    n = int(input())
    square_nums = []
    dp = [1] + [0] * n
    for i in range(1, int(n**0.5)+1):
        square_nums.append(i**2)
        dp[i**2] = 1
    for i in range(2, n + 1):
        if dp[i] == 1: continue
        dp[i] = min(dp[i - num] for num in square_nums[:int(i**0.5)]) + 1
    print(dp[n])

if __name__ == "__main__":
    main()