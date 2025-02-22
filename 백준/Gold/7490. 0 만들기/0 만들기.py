import sys
input = sys.stdin.readline

def dfs(n, i, string, value, last):
    if n < i:
        if value == 0:
            print(string)
        return
    now = 10*last + (i if last>0 else -i)
    dfs(n, i+1, f"{string} {i}", value - last + now, now)
    dfs(n, i + 1, f"{string}+{i}", value + i, i)
    dfs(n, i + 1, f"{string}-{i}", value - i, -i)

def main():
    for _ in range(int(input())):
        n = int(input())
        dfs(n, 2, '1', 1, 1)
        print()

if __name__ == "__main__":
    main()