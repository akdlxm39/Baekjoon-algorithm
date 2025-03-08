import sys
input = sys.stdin.readline

#       0   1
# S0:   1   2
# S1:   -   0
# S2:   3   -
# S3:   4   -
# S4:   4   5
# S5:   1   6
# S6:   7   6
# S7:   4   0

def main():
    re = [(1, 2), (-1, 0), (3, -1), (4, -1), (4, 5), (1, 6), (7, 6), (4, 0)]
    s = input().rstrip()
    state = 0
    for c in s:
        if state == -1:
            break
        i = int(c)
        state = re[state][i]
    if state == 0 or state == 5 or state == 6:
        print("SUBMARINE")
    else:
        print("NOISE")


if __name__ == "__main__":
    main()