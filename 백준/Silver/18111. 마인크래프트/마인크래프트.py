import sys
input = sys.stdin.readline

def main():
    n, m, block = map(int, input().split())
    heights = dict()
    for _ in range(n):
        for x in map(int, input().split()):
            heights[x] = heights.get(x, 0) + 1
    height = min(heights.keys())
    size = n*m
    time = 0
    for cur, cnt in heights.items():
        tmp = (cur - height) * cnt
        time += 2 * tmp
        block += tmp
    need = heights[height]
    ans = (time, height)
    height += 1
    while block >= size:
        time += 3*need - 2*size
        block -= size
        if time <= ans[0]:
            ans = (time, height)
        if height in heights:
            need += heights[height]
        height += 1
    print(*ans)

if __name__ == "__main__":
    main()