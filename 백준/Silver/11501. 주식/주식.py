import sys
input = sys.stdin.readline

def main():
    T = int(input())
    for _ in range(T):
        n = int(input())
        price = list(map(int, input().split()))
        high = price[-1]
        answer = 0
        for p in price[-2::-1]:
            if high >= p:
                answer += high - p
            else:
                high = p
        print(answer)

if __name__ == "__main__":
    main()