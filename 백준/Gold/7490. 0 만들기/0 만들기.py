import sys
input = sys.stdin.readline

def eval(string):
    nums = []
    cur = 0
    while cur < len(string):
        pre = cur
        cur += 1
        while cur < len(string) and string[cur] != '+' and string[cur] != '-':
            cur += 1
        nums.append(int(string[pre:cur]))
    return sum(nums)

def dfs(n, i, string):
    if n < i:
        if eval(string.replace(' ', '')) == 0:
            print(string)
        return
    for x in [' ', '+', '-']:
        dfs(n, i+1, string + x + str(i))

def main():
    for _ in range(int(input())):
        n = int(input())
        dfs(n, 2, '1')
        print()

if __name__ == "__main__":
    main()