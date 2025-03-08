import sys
input = sys.stdin.readline
gcd = lambda a, b : a if b else gcd(b, a%b)

def get_pi(p):
    n = len(p)
    pi = [0]*n
    j = 0
    for i in range(1, n):
        while j > 0 and p[i] != p[j]:
            j = pi[j-1]
        if p[i] == p[j]:
            j += 1
            pi[i] = j
    return pi

def kmp(n, t, p):
    j = 0
    cnt = 0
    pi = get_pi(p)
    for i in range(2*n-1):
        while j > 0 and t[i] != p[j]:
            j = pi[j-1]
        if j == n-1:
            cnt += 1
            j = pi[j]
        elif t[i] == p[j]:
            j += 1
    return cnt

def main():
    n = int(input())
    s1 = input().rstrip().replace(' ', '')
    s2 = input().rstrip().replace(' ', '') * 2
    s2 = s2[:-1]
    cnt =kmp(n, s2, s1)
    x = gcd(cnt, n)
    print(cnt//x,'/',n//x,sep='')

if __name__ == "__main__":
    main()