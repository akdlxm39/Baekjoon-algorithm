import sys
input = sys.stdin.readline

def main():
    n = int(input())
    building_list = list(map(int, input().split()))
    can_see_cnt = [0]*n
    for i in range(n):
        m = -1_000_000_000
        for j in range(i+1, n):
            cur_m = (building_list[j] - building_list[i])/(j-i)
            if cur_m > m:
                can_see_cnt[i] += 1
                can_see_cnt[j] += 1
                m = cur_m
    print(max(can_see_cnt))

if __name__ == "__main__":
    main()