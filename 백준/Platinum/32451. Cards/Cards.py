import sys

input = sys.stdin.readline


def update(n, tree, idx):
    while idx <= n:
        tree[idx] += 1
        idx += idx & -idx


def range_sum(tree, idx):
    res = 0
    while 0 < idx:
        res += tree[idx]
        idx -= idx & -idx
    return res


def main():
    n = int(input())
    cards = list(zip(map(int, input().split()), map(int, input().split())))
    cards.sort()

    tree = [0] * (n + 1)
    gap = 0
    arr = [0] * n
    for i in range(n - 1, -1, -1):
        tmp = range_sum(tree, cards[i][1])
        arr[i] = cards[i][1] - tmp - 1
        gap += tmp
        update(n, tree, cards[i][1])
    ans = []
    i = n - 1
    for j in range(n - 1, -1, -1):
        t = (i - arr[j]) * 2
        if t > gap:
            idx = i
            while idx > 0 and gap > 0:
                if cards[idx][1] < cards[idx - 1][1]:
                    gap -= 2
                cards[idx], cards[idx - 1] = cards[idx - 1], cards[idx]
                idx -= 1
            if gap == 0:
                break
        else:
            ans.append(cards[i])
            cards.pop()
            gap -= t
            i -= 1
    if gap != 0:
        print("No")
    else:
        ans += cards
        ans = list(zip(*ans))
        print("Yes")
        print(*ans[0])
        print(*ans[1])


if __name__ == "__main__":
    main()