import sys
input = sys.stdin.readline

def main():
    n, k = map(int, input().split())
    seq = list(input().split())
    using = []
    ans = 0
    for i, x in enumerate(seq):
        if x in using:
            continue
        elif len(using) < n:
            using.append(x)
        elif x not in using:
            opt, val = -1, 0
            for j, y in enumerate(using):
                if y not in seq[i:]:
                    opt = j
                    break
                idx = seq.index(y, i)
                if val < idx:
                    opt = j
                    val = idx
            using[opt] = x
            ans += 1
    print(ans)

if __name__ == "__main__":
    main()