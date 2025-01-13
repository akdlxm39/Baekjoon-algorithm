import sys
from collections import deque
input = sys.stdin.readline

def main():
    T = int(input())
    for i in range(1, T + 1):
        n, k = map(int, input().split())
        dict = {n:1}
        q = deque([n])
        while k > 0 and q:
            cur = q.popleft()
            cnt = dict[cur]
            max_gap, min_gap = cur // 2, (cur - 1) // 2
            k -= cnt
            if max_gap == 0:
                continue
            if max_gap in q:
                dict[max_gap] += cnt
            else:
                dict[max_gap] = cnt
                q.append(max_gap)
            if min_gap == 0:
                continue
            if min_gap in q:
                dict[min_gap] += cnt
            else:
                dict[min_gap] = cnt
                q.append(min_gap)
        print(f"Case #{i}:", max_gap, min_gap)

if __name__ == "__main__":
    main()