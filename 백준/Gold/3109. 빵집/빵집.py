import sys
input = sys.stdin.readline

def pipelining(c, map_, i, j):
    if j == c-1:
        return True
    nj = j + 1
    for ni in range(i-1, i+2):
        if map_[ni][nj]: continue
        map_[ni][nj] = True
        if pipelining(c, map_, ni, nj):
            return True
    return False

def main():
    r, c = map(int, input().split())
    map_ = [[True]*c]
    for _ in range(r):
        line = list(map(lambda x: x=='x', input().rstrip()))
        map_.append(line)
    map_.append([True]*c)
    ans = 0
    for i in range(r):
        if pipelining(c, map_, i, 0):
            map_[i][0] = True
            ans += 1
    print(ans)
if __name__ == "__main__":
    main()