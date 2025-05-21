import sys
input = sys.stdin.readline

def sol(size, paren, idx):
    ans = 0
    i = idx+1
    while i < size:
        if paren[i] == '(' or paren[i] == '[':
            tmp, i = sol(size, paren, i)
            if tmp == 0: return 0, -1
            ans += tmp
        elif paren[i] == ')' and paren[idx] == '(':
            res = 2 if ans == 0 else ans*2
            return res, i+1
        elif paren[i] == ']' and paren[idx] == '[':
            res = 3 if ans == 0 else ans*3
            return res, i+1
        else:
            return 0, -1
    return 0, -1

def main():
    parentheses = '(' + input().rstrip() + ')'
    ans, i = sol(len(parentheses), parentheses, 0)
    print(ans//2 if i==len(parentheses) else 0)

if __name__ == "__main__":
    main()