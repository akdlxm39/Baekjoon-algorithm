import sys
input = sys.stdin.readline

def main():
    min_num, max_num = map(int, input().split())
    num_range = max_num - min_num + 1
    nums = [True]*num_range
    prime_size = int(max_num**0.5)+1
    prime_nums = [False] * 2 + [True] * (prime_size - 1)
    for x in range(2, prime_size):
        if not prime_nums[x]:
            continue
        prime_nums[x::x] = [False] * (prime_size // x)
        x *= x
        tmp_i = ((min_num-1)//x+1)*x - min_num
        nums[tmp_i::x] = [False]*((num_range-tmp_i-1)//x+1)
    print(sum(nums))

if __name__ == "__main__":
    main()