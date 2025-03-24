import sys
input = sys.stdin.readline

def main():
    n = int(input())
    lamp1 = input().rstrip()
    lamp2 = input().rstrip()
    # state 0: !click and !need / 1: !click and need / 2: click and !need / 3: click and need
    case1_flag, case2_flag = (False, False), (False, True)
    case1_cnt = case2_cnt = 0
    for i in range(n):
        case1_cnt += case1_flag[1]
        case1_flag = (case1_flag[1], (case1_flag[0]==case1_flag[1])!=(lamp1[i]==lamp2[i]))
        case2_cnt += case2_flag[1]
        case2_flag = (case2_flag[1], (case2_flag[0]==case2_flag[1])!=(lamp1[i]==lamp2[i]))
    if case1_flag[1] and case2_flag[1]:
        print(-1)
    elif case1_flag[1]:
        print(case2_cnt)
    else:
        print(case1_cnt)

if __name__ == "__main__":
    main()