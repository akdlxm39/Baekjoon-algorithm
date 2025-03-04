import sys
input = sys.stdin.readline

def find_suzerain(suzerain_of, k):
    if suzerain_of[k] != k:
        suzerain_of[k] = find_suzerain(suzerain_of, suzerain_of[k])
    return suzerain_of[k]

def war(suzerain_of, win, lose):
    win_s = find_suzerain(suzerain_of, win)
    lose_s = find_suzerain(suzerain_of, lose)
    if win_s != lose_s:
        suzerain_of[lose_s] = win_s
    else:
        suzerain_of[lose] = win
        suzerain_of[win] = win

def main():
    n, m = map(int, input().split())
    kingdoms_dict = {input().rstrip():i for i in range(n)}
    suzerain_of = list(range(n))
    for _ in range(m):
        k1, k2, w = input().rstrip().split(',')
        if w == '1':
            war(suzerain_of, kingdoms_dict[k1], kingdoms_dict[k2])
        else:
            war(suzerain_of, kingdoms_dict[k2], kingdoms_dict[k1])
    cnt = 0
    suzerains = []
    for k, i in kingdoms_dict.items():
        if i == find_suzerain(suzerain_of, i):
            cnt += 1
            suzerains.append(k)
    print(cnt, '\n'.join(sorted(suzerains)), sep='\n')

if __name__ == "__main__":
    main()