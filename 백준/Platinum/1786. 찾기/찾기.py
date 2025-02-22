import sys
input = sys.stdin.readline

def getPi(p):
    pi = [0] * len(p)
    j = 0
    for i in range(1, len(p)):
        while j > 0 and p[i] != p[j]:
            j = pi[j-1]
        if p[i] == p[j]:
            pi[i] = j = j + 1
    return pi

def kmp(t, p):
    n, m = len(t), len(p)-1
    cnt = 0
    find = []
    pi = getPi(p)
    j = 0
    for i in range(n):
        while j > 0 and t[i] != p[j]:
            j = pi[j-1]
        if j == m:
            cnt += 1
            find.append(i-m+1)
            j = pi[j]
        elif t[i] == p[j]:
            j += 1
    return cnt, find

def main():
    T = input().rstrip()
    P = input().rstrip()
    cnt, find = kmp(T, P)
    print(cnt, ' '.join(map(str, find)), sep='\n')

if __name__ == "__main__":
    main()