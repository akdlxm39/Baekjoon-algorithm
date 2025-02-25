import sys
input = sys.stdin.readline

def nostar(s):
    if len(s)%2:
        return False
    half = len(s)//2 - s.count('(')
    cnt = 0
    for i, c in enumerate(s):
        if c == '(':
            cnt += 1
        elif c == '?' and half > 0:
            cnt += 1
            half -= 1
        else:
            cnt -= 1
        if cnt < 0:
            return False
    return True if cnt == 0 else False

def star(s, x):
    cnt = 0
    for c in s:
        if c == x or c == '?':
            cnt += 1
        else:
            cnt -= 1
        if cnt < 0:
            return False
    return True

def main():
    for _ in range(int(input())):
        s = input().rstrip().split('*')
        check = False
        if len(s) == 1:
            check = nostar(s[0])
        else:
            s1, s2 = s[0], s[-1]
            if s1 == '' and s2 == '':
                check = True
            elif s1 == '':
                check = star(reversed(s2), ')')
            elif s2 == '':
                check = star(s1, '(')
            else:
                check = star(reversed(s2), ')') and star(s1, '(')
        print("YES" if check else "NO")

if __name__ == "__main__":
    main()