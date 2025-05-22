import sys
input = sys.stdin.readline

def pipelining(c, map_, i, j):
    map_[i][j] = True
    nj = j + 1
    if nj == c:
        return True
    for ni in range(i-1, i+2):
        if not map_[ni][nj] and pipelining(c, map_, ni, nj):
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
    for i in range(1, r+1):
        if pipelining(c, map_, i, 0):
            ans += 1
    print(ans)
if __name__ == "__main__":
    main()