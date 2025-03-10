import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def get_substrings(n):
    s = str(n)
    res = set()
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            res.add(int(s[i:j]))
    res.remove(n)
    if 0 in res:
        res.remove(0)
    return sorted(res)

def main():
    n = int(input())
    how_win = [-1]*(n+1)
    for i in range(10, n+1):
        for k in get_substrings(i):
            if how_win[i-k] == -1:
                how_win[i] = k
                break
    print(how_win[-1])

if __name__ == "__main__":
    main()