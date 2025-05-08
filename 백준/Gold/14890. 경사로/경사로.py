import sys
input = sys.stdin.readline

def check_road(n, l, road):
    length = 0
    pre_h = road[0]
    for i in range(n):
        if road[i] == pre_h:
            length += 1
        elif road[i] == pre_h+1:
            if length < l:
                return False
            pre_h = road[i]
            length = 1
        elif road[i] == pre_h-1:
            if length < 0:
                return False
            pre_h = road[i]
            length = -l+1
        else:
            return False
    return length >= 0

def main():
    n, l = map(int, input().split())
    map_ = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    for road in map_:
        if check_road(n, l, road):
            ans += 1
    for road in zip(*map_):
        if check_road(n, l, road):
            ans += 1
    print(ans)

if __name__ == "__main__":
    main()