import sys
input = sys.stdin.readline

num36 = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
         'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G': 16, 'H': 17, 'I': 18,
         'J': 19, 'K': 20, 'L': 21, 'M': 22, 'N': 23, 'O': 24, 'P': 25, 'Q': 26, 'R': 27,
         'S': 28, 'T': 29, 'U': 30, 'V': 31, 'W': 32, 'X': 33, 'Y': 34, 'Z': 35}

def main():
    n = int(input())
    num_cnt = [0] * 36
    ans = 0
    for _ in range(n):
        s = input().rstrip()
        x = 1
        for c in s[::-1]:
            ans += num36[c]*x
            num_cnt[num36[c]] += x
            x *= 36
    increase = [0] * 36
    for c in num36.keys():
        increase[num36[c]] = num_cnt[num36[c]] * (num36['Z'] - num36[c])
    k = int(input())
    ans += sum(sorted(increase, reverse=True)[:k])
    result = ''
    while ans:
        result = str(list(num36.keys())[ans%36]) + result
        ans //= 36
    print(result if result else 0)

if __name__ == "__main__":
    main()