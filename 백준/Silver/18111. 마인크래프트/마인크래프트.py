import sys
input = sys.stdin.readline

def main():
    n, m, b = map(int, input().split())
    heights = dict()
    for _ in range(n):
        for x in map(int, input().split()):
            heights[x] = heights.get(x, 0) + 1
    min_height = min(heights.keys())
    max_height = max(heights.keys())
    size = n*m
    
    time = 0
    block = b
    for cur, cnt in heights.items():
        tmp = (cur - min_height) * cnt
        time += 2 * tmp
        block += tmp
    need = heights[min_height]
    ans = (time, min_height)
    for height in range(min_height+1, max_height+1):
        if block >= size:
            time += 3*need - 2*size
            block -= size
            if time <= ans[0]:
                ans = (time, height)
        else:
            break
        if height in heights:
            need += heights[height]
    print(*ans)

if __name__ == "__main__":
    main()