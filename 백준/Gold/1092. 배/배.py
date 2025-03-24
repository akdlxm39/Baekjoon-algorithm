import sys
input = sys.stdin.readline

def main():
    n = int(input())
    cranes = sorted(map(int, input().split()), reverse=True)
    m = int(input())
    boxes = sorted(map(int, input().split()), reverse=True)
    if cranes[0] < boxes[0]:
        print(-1)
        return
    max_cnt = []
    i = 0
    for crane in cranes[1:]:
        cnt = i
        while i < m and crane < boxes[i]:
            i += 1
        max_cnt.append(i-cnt)
        if i == m:
            break
    else:
        max_cnt.append(m-i)
    h = remain = 0
    for w, cur_cnt in enumerate(max_cnt, 1):
        cur = cur_cnt - remain
        if cur > h:
            cur -= h
            h += (cur-1)//w+1
            remain = (w-cur%w) if cur%w else 0
        else:
            remain = h-cur
    print(h)

if __name__ == "__main__":
    main()