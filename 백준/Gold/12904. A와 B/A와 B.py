import sys
input = sys.stdin.readline

def main():
    s = list(input().rstrip())
    t = list(input().rstrip())
    while t:
        if s == t:
            print(1)
            break
        elif len(s) == len(t):
            print(0)
            break
        if t[-1] == 'A':
            t.pop()
        else:
            t.pop()
            t.reverse()

if __name__ == "__main__":
    main()