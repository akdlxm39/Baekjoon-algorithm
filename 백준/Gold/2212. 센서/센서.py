import sys
input = sys.stdin.readline

def main():
    n = int(input())
    k = int(input())
    sensor = sorted(map(int, input().split()))
    gap = sorted([sensor[i] - sensor[i-1] for i in range(1, n)])
    print(sum(gap[:n-k]))

if __name__ == "__main__":
    main()