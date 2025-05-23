import sys
input = sys.stdin.readline
dirs = {'R':(1,0), 'L':(-1,0), 'B':(0,-1), 'T':(0,1),
        'RT':(1,1), 'LT':(-1,1), 'RB':(1,-1), 'LB':(-1,-1)}

def main():
    king, stone, n = input().split()
    king_a, king_n = ord(king[0])-64, int(king[1])
    stone_a, stone_n = ord(stone[0])-64, int(stone[1])
    for _ in range(int(n)):
        da, dn = dirs[input().rstrip()]
        nxt_king_a, nxt_king_n = king_a+da, king_n+dn
        if not (1<=nxt_king_a<=8 and 1<=nxt_king_n<=8):
            continue
        if nxt_king_a == stone_a and nxt_king_n == stone_n:
            nxt_stone_a, nxt_stone_n = stone_a+da, stone_n+dn
            if not (1<=nxt_stone_a<=8 and 1<=nxt_stone_n<=8):
                continue
            stone_a, stone_n = nxt_stone_a, nxt_stone_n
        king_a, king_n = nxt_king_a, nxt_king_n
    print(chr(king_a+64), king_n, sep='')
    print(chr(stone_a+64), stone_n, sep='')

if __name__ == "__main__":
    main()