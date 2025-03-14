import sys
from math import sqrt
input = sys.stdin.readline

def main():
    input()
    for x in map(int, input().split()):
        y = int(sqrt(x))
        print(int(y*y == x), end=' ')

if __name__ == "__main__":
    main()