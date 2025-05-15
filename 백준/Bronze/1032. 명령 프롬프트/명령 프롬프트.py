import sys
input = sys.stdin.readline

def main():
    n = int(input())
    ans = list(input())
    size = len(ans)
    for _ in range(n-1):
        word = input()
        for i in range(size):
            if ans[i] != word[i]:
                ans[i] = '?'
    print(''.join(ans))

if __name__ == "__main__":
    main()