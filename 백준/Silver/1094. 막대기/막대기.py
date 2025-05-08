import sys
input = sys.stdin.readline

def main():
    print(bin(int(input())).count('1'))

if __name__ == "__main__":
    main()