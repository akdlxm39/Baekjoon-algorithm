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
    while cranes and cranes[-1] < boxes[-1]:
        cranes.pop()
        n -= 1
    ans = 0
    while m:
        i = 0
        for j in range(n):
            if m == 0:
                break
            elif cranes[j] < boxes[-1]:
                n = j
                break
            while i < m and cranes[j] < boxes[i]:
                i += 1
            boxes.pop(i)
            m -= 1
        ans += 1
    print(ans)

if __name__ == "__main__":
    main()