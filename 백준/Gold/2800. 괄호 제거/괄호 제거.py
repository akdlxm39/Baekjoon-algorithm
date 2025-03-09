import sys
input = sys.stdin.readline

def dfs(s, pairs, i, exps):
    if i == len(pairs):
        exps.append(''.join(s))
        return
    dfs(s, pairs, i + 1, exps)
    s[pairs[i][0]] = ''
    s[pairs[i][1]] = ''
    dfs(s, pairs, i + 1, exps)
    s[pairs[i][0]] = '('
    s[pairs[i][1]] = ')'
    return

def main():
    s = list(input().rstrip())
    pairs = []
    stack = []
    for i, c in enumerate(s):
        if c == '(':
            stack.append(i)
        elif c == ')':
            pairs.append((stack.pop(), i))
    exps = []
    dfs(s, pairs, 0, exps)
    ans = sorted(set(exps))
    print(*ans[1:], sep='\n')

if __name__ == "__main__":
    main()