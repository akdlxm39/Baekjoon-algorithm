import sys
input = sys.stdin.readline

def dfs(n, i, value, last, string):
    if n < i:
        if value == 0:
            print(string)
        return
    now = 10*last + (i if last>0 else -i)
    dfs(n, i+1, value-last+now, now, f"{string} {i}")
    dfs(n, i+1, value+i, i, f"{string}+{i}")
    dfs(n, i+1, value-i, -i, f"{string}-{i}")

def main():
    for _ in range(int(input())):
        dfs(int(input()), 2, 1, 1, '1')
        print()

if __name__ == "__main__":
    main()