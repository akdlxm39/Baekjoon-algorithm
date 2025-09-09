import sys
from functools import reduce
from itertools import combinations

input = sys.stdin.readline
alpha_bit = dict((chr(97 + i), 1 << i) for i in range(26))
alpha_to_bit = lambda acc, cur: acc | alpha_bit[cur]


def bruteforce(k, needs):
    learn = reduce(alpha_to_bit, 'acint', 0)
    res = 0
    for alpha2 in combinations('bdefghjklmopqrsuvwxyz', k):
        cur_learn = reduce(alpha_to_bit, alpha2, learn)
        tmp = sum(1 for n in needs if n == n & cur_learn)
        if tmp > res:
            res = tmp
    return res


def main():
    n, k = map(int, input().split())
    if k < 5:
        print(0)
        return
    k -= 5
    needs = [reduce(alpha_to_bit, input().rstrip(), 0) for _ in range(n)]
    print(bruteforce(k, needs))


if __name__ == "__main__":
    main()
