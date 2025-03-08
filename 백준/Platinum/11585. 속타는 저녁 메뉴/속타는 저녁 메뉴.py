import sys
input = sys.stdin.readline

def main():
    n = int(input())
    s = input().rstrip().replace(' ', '')
    x = (s*2).find(s, 1)
    print('1/'+str(x))

if __name__ == "__main__":
    main()