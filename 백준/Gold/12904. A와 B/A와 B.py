import sys
input = sys.stdin.readline

def main():
    s = list(input().rstrip())
    t = list(input().rstrip())
    dir = 1
    while t:
        if s == t:
            print(1)
            break
        if t[-1] == 'A':
            t.pop()
        else:
            t.pop()
            t.reverse()
    else:
        print(0)

if __name__ == "__main__":
    main()