import sys
input = sys.stdin.readline

def main():
    n = int(input())
    a = b = 1
    for _ in range(n-1):
        a, b = b, (a*2 + b) % 10007
    print(b)

if __name__ == "__main__":
    main()