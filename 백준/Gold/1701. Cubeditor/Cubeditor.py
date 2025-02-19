import sys
input = sys.stdin.readline

def getMaxPi(p):
    pi = [0] * len(p)
    j = 0
    for i in range(1, len(p)):
        while j > 0 and p[i] != p[j]:
            j = pi[j-1]
        if p[i] == p[j]:
            pi[i] = j = j + 1
    return max(pi)

def main():
    s = input().rstrip()
    length = len(s)
    ans = 0
    i = 0
    while i < length - ans:
        ans = max(ans, getMaxPi(s[i:]))
        i += 1
    print(ans)

if __name__ == "__main__":
    main()