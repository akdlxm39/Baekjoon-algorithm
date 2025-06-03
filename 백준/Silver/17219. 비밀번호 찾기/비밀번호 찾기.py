import sys
input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    pw_dict = dict(tuple(input().split()) for _ in range(n))
    ans = [pw_dict[input().rstrip()] for _ in range(m)]
    print('\n'.join(ans))

if __name__ == "__main__":
    main()