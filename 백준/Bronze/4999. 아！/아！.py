import sys

input = sys.stdin.readline


def main():
    print('go' if len(input()) >= len(input()) else 'no')


if __name__ == "__main__":
    main()
