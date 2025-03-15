import sys
input = sys.stdin.readline

def main():
    exp = '(' + input().rstrip().replace(' ', '') + ')'
    stack = []
    alpha = 0
    oper = 0
    flag = 0
    for x in exp:
        if 'a' <= x <= 'z':
            if alpha == oper:
                alpha += 1
            else:
                flag = -1
                break
        elif x in '+-*/%':
            if oper < alpha:
                oper += 1
            else:
                flag = -1
                break
        elif x == '(':
            if alpha == oper:
                stack.append((alpha, oper))
                alpha = oper = 0
            else:
                flag = -1
                break
        elif x == ')':
            if alpha == oper:
                flag = -1
                break
            elif alpha + oper != 3:
                flag = 1
            if stack:
                alpha, oper = stack.pop()
                alpha += 1
            else:
                flag = -1
                break
        else:
            flag = -1
            break
    if flag == -1 or stack:
        print('error')
    elif alpha == 1 and oper == 0 and flag == 0:
        print('proper')
    else:
        print('improper')

if __name__ == "__main__":
    main()