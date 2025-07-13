import sys
input = sys.stdin.readline

def main():
    n, c = map(int, input().split())
    m = int(input())
    packages = sorted((tuple(map(int, input().split())) for _ in range(m)), key = lambda x: (x[1], x[0]))
    ans = 0
    carries = [0] * (n + 1)
    for s, d, w in packages:
        can_carry = min(w, min(c - carries[i] for i in range(s, d)))
        for i in range(s, d):
            carries[i] += can_carry
        ans += can_carry
    print(ans)

if __name__ == "__main__":
    main()