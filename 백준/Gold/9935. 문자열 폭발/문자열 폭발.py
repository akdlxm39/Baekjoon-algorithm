import sys
input = sys.stdin.readline

def main():
    s = input().rstrip()
    bomb = list(input().rstrip())
    n, m = len(s), len(bomb)
    ans = []
    for c in s:
        ans.append(c)
        if ans[-m:] == bomb:
            for _ in range(m):
                ans.pop()
    print(''.join(ans) if ans else "FRULA")

if __name__ == "__main__":
    main()