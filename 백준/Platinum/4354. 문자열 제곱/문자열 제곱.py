import sys
input = sys.stdin.readline

def main():
    while True:
        s = input().rstrip()
        if s == '.':
            break
        print(len(s)//(s+s).find(s,1))

if __name__ == "__main__":
    main()