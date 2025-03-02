import sys
input = sys.stdin.readline

def main():
    for _ in range(int(input())):
        w = input().rstrip()
        k = int(input())
        cp = dict((chr(c), []) for c in range(97, 123))
        for i, c in enumerate(w):
            cp[c].append(i)
        ans1, ans2 = 10000, 0
        flag = False
        for c, l in cp.items():
            if len(l) < k:
                continue
            flag = True
            for x, y in zip(l, l[k-1:]):
                ans1 = min(ans1, y - x + 1)
                ans2 = max(ans2, y - x + 1)
        if flag:
            print(ans1, ans2)
        else:
            print(-1)

if __name__ == "__main__":
    main()