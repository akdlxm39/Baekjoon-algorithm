import sys
input = sys.stdin.readline

def get_pairs(pairs, i):
    l, r = pairs[i]
    res = [l]
    i += 1
    while i < len(pairs) and pairs[i][1] < r:
        tmp, j = get_pairs(pairs, i)
        res.append(tmp)
        i = j
    res.append(r)
    return res, i

def dfs(s, pairs):
    if not pairs:
        return ['']
    res = ['']
    prev_r = pairs[0]+1
    for pair in pairs[1:-1]:
        cur_l, cur_r = pair[0], pair[-1]
        tmp_s = s[prev_r:cur_l]
        exps = dfs(s, pair)
        res = [x+tmp_s+exp for x in res for exp in exps]
        prev_r = cur_r+1
    tmp_s = s[prev_r:pairs[-1]] if s[prev_r:pairs[-1]] else ''
    res = ['('+x+tmp_s+')' for x in res] + [x+tmp_s for x in res]
    return res

def main():
    s = input().rstrip()
    pairs = []
    stack = []
    for i, c in enumerate(s):
        if c == '(':
            stack.append(i)
        elif c == ')':
            pairs.append((stack.pop(), i))
    pairs, _ = get_pairs(sorted(pairs), 0)
    exps = dfs(s, pairs)
    ans = [s[:pairs[0]] + x + s[pairs[-1]+1:] for x in exps]
    ans = sorted(set(ans))
    print(*ans[1:],sep='\n')

if __name__ == "__main__":
    main()