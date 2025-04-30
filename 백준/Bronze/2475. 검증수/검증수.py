import sys
input = sys.stdin.readline

def main():
    print(sum(map(lambda x: int(x)**2, input().split()))%10)

if __name__ == "__main__":
    main()