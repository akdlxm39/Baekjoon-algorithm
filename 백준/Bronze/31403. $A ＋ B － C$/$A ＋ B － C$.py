import sys

input = sys.stdin.readline


def main():
    a, b, c = (input().rstrip() for _ in range(3))
    print(int(a) + int(b) - int(c))
    print(int(a + b) - int(c))


if __name__ == "__main__":
    main()
