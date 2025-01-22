import sys
input = sys.stdin.readline

def solve(now, depth, dir, cnt):
    if cnt == 0:
        pass
    elif depth < 0:
        now[:] = ['-1']
    elif cnt % 2 == 0:
        solve(now, depth-1, dir, cnt//2)
    elif now[depth] == dir[0]:
        now[depth] = dir[1]
        solve(now, depth - 1, dir, cnt//2)
    elif now[depth] == dir[2]:
        now[depth] = dir[3]
        solve(now, depth - 1, dir, cnt//2)
    elif now[depth] == dir[1]:
        now[depth] = dir[0]
        solve(now, depth - 1, dir, cnt//2+1)
    elif now[depth] == dir[3]:
        now[depth] = dir[2]
        solve(now, depth - 1, dir, cnt//2+1)

def main():
    d, piece = input().split()
    d = int(d)
    piece = list(piece)
    dx, dy = map(int, input().split())
    dirs = [('2', '1', '3', '4'), #right
           ('1', '2', '4', '3'), #left
           ('3', '2', '4', '1'), #up
           ('2', '3', '1', '4')] #down
    solve(piece, d-1, dirs[dx<0], abs(dx))
    if piece != ['-1']:
        solve(piece, d-1, dirs[(dy<0)+2], abs(dy))
    print(''.join(piece))


if __name__ == "__main__":
    main()