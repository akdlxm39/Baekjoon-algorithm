import sys
input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    book = list(map(int, input().split()))
    left = sorted([-x for x in book if x < 0], reverse=True)
    right = sorted([x for x in book if x > 0], reverse=True)
    answer = 0
    for x in left[::m]:
        answer += x * 2
    for x in right[::m]:
        answer += x * 2
    answer -= max(left + right)
    print(answer)

if __name__ == "__main__":
    main()

    