import sys
input = sys.stdin.readline

def main():
    input()
    for x in map(int, input().split()):
        print(int(x == (int(x**0.5)**2)), end=' ')

if __name__ == "__main__":
    main()