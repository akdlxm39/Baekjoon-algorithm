import sys
input = sys.stdin.readline

def main():
    while True:
        n = int(input())
        if n == 0:
            break
        reversed_n = 0
        tmp = n
        while tmp:
            reversed_n *= 10
            reversed_n += tmp % 10
            tmp //= 10
        if n == reversed_n:
            print('yes')
        else:
            print('no')


if __name__ == "__main__":
    main()