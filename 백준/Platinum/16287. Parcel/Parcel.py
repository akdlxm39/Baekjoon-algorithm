import sys

input = sys.stdin.readline


def main():
    w, n = map(int, input().split())
    items = list(map(int, input().split()))
    double = {}
    for i in range(n - 1):
        for j in range(i+1, n):
            tmp = items[i] + items[j]
            if tmp >= w or tmp in double: continue
            double[tmp] = (items[i], items[j])
    for i in range(n-1):
        for j in range(i + 1, n):
            a, b = items[i], items[j]
            rest = w - a - b
            if rest not in double: continue
            c, d = double[rest]
            if a!=c and a!=d and b!=c and b!=d:
                print("YES")
                return
    print("NO")


if __name__ == "__main__":
    main()
