import sys
input = sys.stdin.readline

def main():
    n = int(input())
    month = [0, 0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
    flowers = []
    for _ in range(n):
        m1, d1, m2, d2 = map(int, input().split())
        flowers.append((month[m1] + d1, month[m2] + d2))
    flowers.sort()

    new = 0
    cnt = 1
    cur = 60
    for s, e in flowers:
        if s <= cur:
            new = max(new, e)
            if new >= 335:
                print(cnt)
                break
        else:
            cur = new
            cnt += 1
            if s <= cur:
                new = e
            else:
                print(0)
                break
    else:
        if new >= 335:
            print(cnt)
        else:
            print(0)

if __name__ == "__main__":
    main()