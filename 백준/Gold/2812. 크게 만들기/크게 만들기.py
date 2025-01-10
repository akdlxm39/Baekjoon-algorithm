import sys
input = sys.stdin.readline

def main():
    n, k = map(int, input().split())
    num = input().rstrip()
    stack = []
    for x in num:
        while stack and k and stack[-1] < x:
            stack.pop()
            k -= 1
        stack.append(x)
    num = ''.join(stack)
    for x in map(str, range(0, 10)):
        if k <= 0:
            break
        cnt = num.count(x)
        num = num.replace(x, '', k)
        k -= cnt
    print(num)
        

if __name__ == "__main__":
    main()