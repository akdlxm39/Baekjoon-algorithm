import sys

input = sys.stdin.readline


def main():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        bit_range = 2 ** m
        dp = [[0] * bit_range for _ in range(n + 1)]
        for i in range(1, n + 1):
            line = input().rstrip()
            broken_bit = 0
            for x in line:
                broken_bit <<= 1
                if x == 'x':
                    broken_bit |= 1
            for cur_bit in range(bit_range):
                if broken_bit & cur_bit: continue
                left_bit = cur_bit << 1
                if left_bit & cur_bit: continue
                right_bit = cur_bit >> 1
                if right_bit & cur_bit: continue
                prev_max = 0
                for prev_bit in range(bit_range):
                    if left_bit & prev_bit or right_bit & prev_bit: continue
                    prev_max = max(prev_max, dp[i-1][prev_bit])
                dp[i][cur_bit] = prev_max + cur_bit.bit_count()
        print(max(dp[-1]))


if __name__ == "__main__":
    main()
