import sys
input = sys.stdin.readline

def main():
    T = int(input())
    for _ in range(T):
        k, n = input().split()
        if '8' not in n and '9' not in n:
            print(k, int(n, 8), int(n), int(n, 16))
        else:
            print(k, 0, int(n), int(n, 16))

if __name__ == "__main__":
    main()