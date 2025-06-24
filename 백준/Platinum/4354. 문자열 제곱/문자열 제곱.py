import sys
input = sys.stdin.readline

def getPi(p):
    pi = [0]*len(p)
    j = 0
    for i in range(1, len(p)):
        while j > 0 and p[i] != p[j]:
            j = pi[j-1]
        if p[i] == p[j]:
            pi[i] = j = j + 1
    return pi

def main():
    while True:
        s = input().rstrip()
        if s == '.':
            break
        pi = getPi(s)
        ans = len(s)/(len(s) - pi[-1])
        print(int(ans) if ans%1==0 else 1)

if __name__ == "__main__":
    main()