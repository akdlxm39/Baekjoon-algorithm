import sys
input = sys.stdin.readline

def main():
    n, k = map(int, input().split())
    price = list(map(int, input().split()))
    diff = sorted([price[i] - price[i-1] for i in range(1, len(price))])
    print(sum(diff[:n-k]))

if __name__ == "__main__":
    main()