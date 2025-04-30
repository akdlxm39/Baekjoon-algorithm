import sys
input = sys.stdin.readline

def main():
    n = int(input())
    a = b = 1
    for i in range(2, n+1):
        a, b = b, (a + b) % 10007
    print(b)

if __name__ == "__main__":
    main()