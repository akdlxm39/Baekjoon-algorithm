import sys
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        ranks = [0]*(n+1)
        for _ in range(n):
            a, b = map(int, input().split())
            ranks[a] = b
        high = ranks[1]
        ans = 1
        for rank in ranks[2:]:
            if rank < high:
                ans += 1
                high = rank
        print(ans)

if __name__ == "__main__":
    main()