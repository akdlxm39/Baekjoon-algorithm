import sys
input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    print(n//m, n%m, sep='\n')

if __name__ == "__main__":
    main()