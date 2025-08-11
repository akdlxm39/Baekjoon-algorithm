import sys

input = sys.stdin.readline
board_score = [0, 2, 4, 6, 8,
               10, 12, 14, 16, 18,
               20, 22, 24, 26, 28,
               30, 32, 34, 36, 38,
               40, 13, 16, 19, 22,
               24, 28, 27, 26, 25,
               30, 35, 0]
board_move = [[0, 1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 6],
              [2, 3, 4, 5, 6, 7], [3, 4, 5, 6, 7, 8],
              [4, 5, 6, 7, 8, 9], [5, 21, 22, 23, 29, 30],
              [6, 7, 8, 9, 10, 11], [7, 8, 9, 10, 11, 12],
              [8, 9, 10, 11, 12, 13], [9, 10, 11, 12, 13, 14],
              [10, 24, 25, 29, 30, 31], [11, 12, 13, 14, 15, 16],
              [12, 13, 14, 15, 16, 17], [13, 14, 15, 16, 17, 18],
              [14, 15, 16, 17, 18, 19], [15, 26, 27, 28, 29, 30],
              [16, 17, 18, 19, 20, 32], [17, 18, 19, 20, 32, 32],
              [18, 19, 20, 32, 32, 32], [19, 20, 32, 32, 32, 32],
              [20, 32, 32, 32, 32, 32], [21, 22, 23, 29, 30, 31],
              [22, 23, 29, 30, 31, 20], [23, 29, 30, 31, 20, 32],
              [24, 25, 29, 30, 31, 20], [25, 29, 30, 31, 20, 32],
              [26, 27, 28, 29, 30, 31], [27, 28, 29, 30, 31, 20],
              [28, 29, 30, 31, 20, 32], [29, 30, 31, 20, 32, 32],
              [30, 31, 20, 32, 32, 32], [31, 20, 32, 32, 32, 32],
              [32, 32, 32, 32, 32, 32]]


def solve(dices, idx, pieces, beginners, can_move, score, ans):
    if idx == 10:
        ans[0] = max(ans[0], score)
        return
    for i, cur in enumerate(pieces):
        nxt = board_move[cur][dices[idx]]
        if not can_move[nxt]: continue
        pieces[i] = nxt
        can_move[cur] += 1
        can_move[nxt] -= 1
        solve(dices, idx + 1, pieces, beginners, can_move, score + board_score[nxt], ans)
        pieces[i] = cur
        can_move[nxt] += 1
        can_move[cur] -= 1
    if beginners:
        nxt = dices[idx]
        if can_move[nxt]:
            can_move[nxt] -= 1
            solve(dices, idx + 1, pieces + [nxt], beginners - 1, can_move, score + board_score[nxt], ans)
            can_move[nxt] += 1


def main():
    dices = list(map(int, input().split()))
    can_move = [1] * 32 + [4]
    ans = [0]
    solve(dices, 0, [], 4, can_move, 0, ans)
    print(ans[0])


if __name__ == "__main__":
    main()
