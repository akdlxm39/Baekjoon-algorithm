import sys
input = sys.stdin.readline

def main():
    n = int(input())
    towers = [int(1e9)] + list(map(int, input().split()))
    stack = [0]
    ans = []
    for i in range(1, n+1):
        while towers[stack[-1]] < towers[i]:
            stack.pop()
        ans.append(stack[-1])
        stack.append(i)
    print(' '.join(map(str, ans)))

if __name__ == "__main__":
    main()