import sys
input = sys.stdin.readline

def main():
    str = input().rstrip()
    p_cnt = 0
    a_flag = False
    for c in str:
        if c == 'P':
            if a_flag:
                p_cnt -= 1
                a_flag = False
            else:
                p_cnt += 1
        elif p_cnt >= 2 and not a_flag:
            a_flag = True
        else:
            p_cnt = -1
            break
    if p_cnt == 1:
        print("PPAP")
    else:
        print("NP")

if __name__ == "__main__":
    main()