import sys
input = sys.stdin.readline

def main():
    n, k = map(int, input().split())
    if n == k:
        print(0)
        return
    dk, time, is_odd = 2, 1, 1
    k += 1
    queue = [n]
    visited = [[0]*500001 for _ in range(2)]
    while k <= 500000:
        nxt_queue = []
        for cur in queue:
            for nxt in [cur-1, cur+1, cur*2]:
                if not (0<=nxt<=500000) or visited[is_odd][nxt]: continue
                visited[is_odd][nxt] = time
                nxt_queue.append(nxt)
        if visited[is_odd][k]:
            print(time)
            break
        k += dk
        is_odd = 1 - is_odd
        dk += 1
        time += 1
        queue = nxt_queue
    else:
        print(-1)

if __name__ == "__main__":
    main()