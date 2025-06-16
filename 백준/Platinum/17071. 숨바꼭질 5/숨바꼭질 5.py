import sys
input = sys.stdin.readline

def main():
    n, k = map(int, input().split())
    dk, time, is_odd = 1, 0, 0
    queue = [n]
    visited = [[-1, -1] for _ in range(500001)]
    visited[n][0] = 0
    while queue:
        if visited[k][is_odd] != -1:
            print(time)
            break
        is_odd = 1-is_odd
        nxt_queue = []
        for cur in queue:
            for nxt in [cur-1, cur+1, cur*2]:
                if not (0<=nxt<=500000) or visited[nxt][is_odd] != -1: continue
                visited[nxt][is_odd] = time
                nxt_queue.append(nxt)
        k += dk
        if k > 500000:
            print(-1)
            break
        dk += 1
        time += 1
        queue = nxt_queue
    else:
        print(-1)

if __name__ == "__main__":
    main()