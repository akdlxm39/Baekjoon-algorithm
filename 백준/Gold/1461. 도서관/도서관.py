import sys
input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    book = list(map(int, input().split()))
    left = sorted([-x for x in book if x < 0], reverse=True)
    right = sorted([x for x in book if x > 0], reverse=True)
    answer = sum(left[::m]) *2 + sum(right[::m]) *2 - max(left + right)
    print(answer)

if __name__ == "__main__":
    main()

    