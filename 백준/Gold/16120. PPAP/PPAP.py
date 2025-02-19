import sys
input = sys.stdin.readline

def main():
    str = input().rstrip()
    stack = []
    for c in str:
        if c == 'P' and stack[-3:] == ['P', 'P', 'A']:
            stack.pop()
            stack.pop()
        else:
            stack.append(c)
    if len(stack) == 1 and stack[0] == 'P':
        print("PPAP")
    else:
        print("NP")

if __name__ == "__main__":
    main()