import sys
input = sys.stdin.readline

def main():
    for _ in range(int(input())):
        w = input().rstrip()
        k = int(input())
        ans1, ans2 = 10000, 0
        if k == 1:
            ans1 = ans2 = 1
        else:
            cp = [[] for _ in range(124)]
            for i, c in enumerate(w):
                cp[ord(c)].append(i)
            for l in cp[97:]:
                if len(l) < k:
                    continue
                for x, y in zip(l, l[k-1:]):
                    ans1 = min(ans1, y - x + 1)
                    ans2 = max(ans2, y - x + 1)
        if ans1 == 10000 or ans2 == 0:
            print(-1)
        else:
            print(ans1, ans2)

if __name__ == "__main__":
    main()