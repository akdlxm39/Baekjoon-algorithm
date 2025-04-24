import sys
from collections import deque
input = sys.stdin.readline

def check(a, b, c):
    for x in a:
        if x != 'A':
            return False
    for x in b:
        if x != 'B':
            return False
    for x in c:
        if x != 'C':
            return False
    return True

def bfs(hanoi:tuple[str,str,str]):
    queue = deque([(hanoi, 0)])
    visited = {hanoi}
    while queue:
        (cur_a, cur_b, cur_c), cnt = queue.popleft()
        if check(cur_a, cur_b, cur_c):
            return cnt
        if cur_a != '':
            nxt_a, tmp = cur_a[:-1], cur_a[-1]
            nxt = (nxt_a, cur_b+tmp, cur_c)
            if nxt not in visited:
                visited.add(nxt)
                queue.append((nxt, cnt + 1))
            nxt = (nxt_a, cur_b, cur_c+tmp)
            if nxt not in visited:
                visited.add(nxt)
                queue.append((nxt, cnt + 1))
        if cur_b != '':
            nxt_b, tmp = cur_b[:-1], cur_b[-1]
            nxt = (cur_a+tmp, nxt_b, cur_c)
            if nxt not in visited:
                visited.add(nxt)
                queue.append((nxt, cnt + 1))
            nxt = (cur_a, nxt_b, cur_c+tmp)
            if nxt not in visited:
                visited.add(nxt)
                queue.append((nxt, cnt + 1))
        if cur_c != '':
            nxt_c, tmp = cur_c[:-1], cur_c[-1]
            nxt = (cur_a+tmp, cur_b, nxt_c)
            if nxt not in visited:
                visited.add(nxt)
                queue.append((nxt, cnt + 1))
            nxt = (cur_a, cur_b+tmp, nxt_c)
            if nxt not in visited:
                visited.add(nxt)
                queue.append((nxt, cnt + 1))

def main():
    hanoi = []
    for i in range(3):
        s = input().split()
        hanoi.append(s[1] if len(s)==2 else '')
    print(bfs(tuple(hanoi)))

if __name__ == "__main__":
    main()