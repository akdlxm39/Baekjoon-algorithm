import sys
input = sys.stdin.readline

def bfs(start):
    queue = [start]
    visited = {start}
    count = 0
    while queue:
        nxt_queue = []
        for cur in queue:
            if cur == '123456780':
                return count
            zero = cur.index('0')
            if zero//3 != 0:
                nxt = cur[:zero-3] + '0' + cur[zero-2:zero] + cur[zero-3] + cur[zero+1:]
                if nxt not in visited:
                    nxt_queue.append(nxt)
                    visited.add(nxt)
            if zero//3 != 2:
                nxt = cur[:zero] + cur[zero+3] + cur[zero+1:zero+3] + '0' + cur[zero+4:]
                if nxt not in visited:
                    nxt_queue.append(nxt)
                    visited.add(nxt)
            if zero%3 != 0:
                nxt = cur[:zero-1] + '0' + cur[zero-1] + cur[zero+1:]
                if nxt not in visited:
                    nxt_queue.append(nxt)
                    visited.add(nxt)
            if zero%3 != 2:
                nxt = cur[:zero] + cur[zero+1] + '0' + cur[zero+2:]
                if nxt not in visited:
                    nxt_queue.append(nxt)
                    visited.add(nxt)
        queue = nxt_queue
        count += 1
    return -1

def main():
    start = ''
    for _ in range(3):
        start += input().rstrip().replace(' ', '')
    print(bfs(start))

if __name__ == "__main__":
    main()